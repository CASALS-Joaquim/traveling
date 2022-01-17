from django.contrib.auth import login
from django.shortcuts import render, redirect

def conn_user(request, user, redirect_uri='/account/profile/'):
    if user is not None and user.is_active:
        login(request, user)
        return redirect(redirect_uri)