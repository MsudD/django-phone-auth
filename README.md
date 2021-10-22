# django-phone-auth
It's a Django application to register and authenticate users using phone number.
CustomUser model created using AbstractUser class.

### Installation
After cloning the repository to your local directory, activate virtual env and install required packages using pip :<br> 
`pip install -r requirements.txt`<br>
then set your database configurations and make migrations.
at last run server and point to the localhost : http://127.0.0.1:8000 there it is.<br> 

> Attention: Product is in the Alpha phase and 'Reset Password' feature isn't functional yet.<br>

### WORKFLOW
* Users register by entering below fields:
  * phone number
  * password

* In the first attempt to login, an SMS will be send to the user phone and will be asked to enter provided code and therefore verify their account.

> Attention: You should provide send_sms module in gateways directory.<br> 
> Attention: You can customize phone field's validation based on your needs located on forms.py<br> 

### Support
It's welcome your supports by giving **Stars** or making **Commits**.

<div dir='rtl'>
<br> 
راهنمای فارسی
</div>
