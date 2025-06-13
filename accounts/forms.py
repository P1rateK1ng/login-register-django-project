from django import forms
from .models import User
from captcha.fields import CaptchaField
from django_recaptcha.fields import ReCaptchaField

class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    captcha = ReCaptchaField()

    class Meta:
        model = User
        fields = ['fullname', 'email', 'login', 'password', 'phone_number']
