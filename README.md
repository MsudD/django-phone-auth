# django-phone-auth
It's a Django application to register and authenticate users using phone number.
CustomUser model created using AbstractUser class.

### Installation
after cloning the repository to your local directory, activate virtual env and install required packages using pip :
`pip install -r requirements.txt`
then set your database configurations and make migrations.
at last run server and point to the localhost : http://127.0.0.1:8000 there it is.

> Attention : Product is in the Alpha phase and 'Reset Password' feature isn't functional yet.

### WORKFLOW
* users register by entering below fields:
  * phone number
  * password

* in first attempt to login, an sms will be send to user phone and will be asked to enter provided code and therefore verify their account.

> Attention : You should provide send_sms module in gateways directory.
> Attention : You can customize phone field's validation based on your needs located on forms.py

### Support
It's welcome to support my work giving **Stars** or make **Commits**

<div dir='rtl'>
راهنمای فارسی
</div>