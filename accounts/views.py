from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import CreateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login as auth_login, get_user_model
from .exceptions import UserNotVerified
from pyotp import OTP,HOTP
from django.contrib import messages
from .gateways.fakesms import send_sms
from .forms import CustomUserCreationForm, VerifyForm

UserModel = get_user_model()

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'

class VerifyMixin:
    @property
    def user(self):
        try:
            user = UserModel.objects.get(phone=self.request.session['phone'])
            return user
        except UserModel.DoesNotExist:
            return 
        except KeyError:
            return

    @property
    def hotp(self):
        secret = self.user.otp_secret
        hotp = HOTP(secret)
        return hotp

    @property       
    def otp_code(self):
        otp_code = self.hotp.at(self.user.otp_counter)
        return otp_code

class VerifyView(VerifyMixin, FormView):
    form_class = VerifyForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/verify.html'

    def get(self, request, *args, **kwargs):
        if self.user:
            return super().get(self, request, *args, **kwargs)
        else :
            return HttpResponseRedirect(self.get_success_url())

    def post(self, request, *args, **kwargs):
        form_otp_code = str(request.POST.get('otp_code'))
        if  self.hotp.verify(form_otp_code, self.user.otp_counter):
            user = self.user
            user.is_verified = True
            user.save()
            messages.success(self.request,'You Verified Successfully. Now Login')
            return super().post(self, request, *args, **kwargs)
        else :
            messages.warning(self.request,'Code entered is not valid.')
            return self.form_invalid(self.form_class)

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['phone']=self.request.session['phone']
        return context

class ResendVerifyView(VerifyMixin, View):
    
    def get(self, request, *args, **kwargs):
        if self.user:
            user = self.user
            user.otp_counter += 1
            user.save()
            send_sms(user.phone, self.otp_code)
        return HttpResponseRedirect(reverse_lazy('verify'))

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get(self, request, *args, **kwargs):
        #if any session there is, remove phone key
        if 'phone' in self.request.session.keys():
            del self.request.session['phone']
        return super().get(self, request, *args, **kwargs)

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        try :
            auth_login(self.request, form.get_user())
        except UserNotVerified:
            """ exception will handeled by middleware"""
            pass
        else:
            return HttpResponseRedirect(self.get_success_url())