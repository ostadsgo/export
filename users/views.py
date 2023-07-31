from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User


from shop.models import Product
from .forms import UserRegisterForm, LoginForm


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "users/login.html"


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("users:login")
    else:
        form = UserRegisterForm()
    return render(request, "users/register.html", {"form": form})


def user_posts(request, username):
    user = User.objects.get(username=username)
    products = Product.objects.filter(user=user)
    return render(request, "user_posts.html", {"products": products})


def dashboard(request):
    products = Product.objects.filter(user=request.user)
    return render(request, "users/dashboard.html", {"products": products})
