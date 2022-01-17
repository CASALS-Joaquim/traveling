from django.shortcuts import render, redirect

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import AnonymousUser, User
from django.views.generic import TemplateView
from django.contrib.auth.forms import AuthenticationForm

from .forms import SignUpForm, LogInForm
from traveling import conn_user

class LogIn(TemplateView):
    template_name = 'account/login.html'

    def post(self, request, **kwargs):
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username = username, password=raw_password)
            return conn_user(request, user)

        return redirect("login")

    def get(self, request, **kwargs):
        conn = conn_user(request, request.user)
        if conn is not None:
            return conn

        form = LogInForm(request)
        return render(request, self.template_name, {
            'form': form
        })

class LogOut(TemplateView):
    def get(self, request, **kwargs):
        logout(request)
        return redirect("/home/")

class Index(TemplateView):
    template_name = 'account/index.html'

    def get(self, request, **kwargs):
        user = request.user
        if user is not None and user.is_active:
            login(request, user)
            return redirect("/account/profile/")

        return render(request, self.template_name, {
            'user': AnonymousUser,
        })

class Profile(TemplateView):
    template_name = 'account/profile.html'

    def get(self, request, **kwargs):
        user = request.user
        if user is not None and user.is_active:
            login(request, user)
            return render(request, self.template_name, {
                'user': user,
            })

        return redirect("/account/")

class SignUp(TemplateView):
    template_name = 'account/signup.html'

    def post(self, request, **kwargs):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            User.objects.create_user(username=username, password=raw_password, email=email)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect(request.GET.get('next', '/account/profile/'))
        
        else:
            return redirect("/account/signup/")


    def get(self, request, **kwargs):
        conn = conn_user(request, request.user)
        if conn is not None:
            return conn

        form = SignUpForm()
        return render(request, self.template_name, {
            'form': form
        })