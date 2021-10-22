from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import PasswordResetForm

UserModel = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    phone = forms.RegexField(regex = '^9\d{9}$', required=True,
                            error_messages = {
                                    'required': 'The Phone field is required.',
                                    'invalid' : 'Enter phone number in 9XX.. format.'
                                }
                            )
    class Meta:
        model = UserModel
        fields = ('phone',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = UserModel
        fields = ('phone',)

class CustomPasswordResetForm(PasswordResetForm):
    pass

class VerifyForm(forms.Form):
    otp_code = forms.CharField(label='Code', max_length=6, required=True,
                        error_messages = {
                            'required' : 'the field is required',
                            'max_length' : 'max length exceeded'
                        }
    
                    )
    