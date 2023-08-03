from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="نام کاربری ",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="رمز ورود",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    def __init__(self, *args, **kwargs):
        self.error_messages["invalid_login"] = "نام کاربری یا رمز ورود اشتباه است"
        super().__init__(*args, **kwargs)


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label="نام کاربری")
    email = forms.EmailField(label="ایمیل")
    password1 = forms.CharField(widget=forms.PasswordInput, label="رمز ورود")
    password2 = forms.CharField(widget=forms.PasswordInput, label="تکرار رمز")
    error_messages = {
        "password_mismatch": "رمز ورود و تکرار رمز عبور یکسان نیستند",
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].error_messages = {
            "required": "لطفا نام کاربری وارد کنید",
            "unique": "این نام کاربری قبلا ثبت شده است",
        }
        self.fields["email"].error_messages = {
            "required": "لطفا آدرس ایمیل خود را وارد کنید",
            "unique": "این آدرس ایمیل قبلا ثبت شده است",
            "invalid": "لطفا یک آدرس ایمیل صحیح وارد کنید",
        }
        self.fields["password1"].error_messages = {
            "required": "لطفا رمز ورود وارد کنید",
        }
        self.fields["password2"].error_messages = {
            "required": "لطفا رمز ورود خود را تکرار کنید",
            "password_mismatch": "رمز ورود و تکرار رمز عبور یکسان نیستند",
        }

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
