from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index.as_view(), name='account'),
    path('profile/', views.Profile.as_view(), name='profile'),
    path('login/', views.LogIn.as_view(), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.LogOut.as_view(), name='logout'),
]