from pyotp import random_base32

# get and save random otp secret after user model created
def customuser_created(sender, instance, created, **kwargs):
    if created:
        instance.otp_secret = random_base32()
        instance.otp_counter = 0
        instance.save()