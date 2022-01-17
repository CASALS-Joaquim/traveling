from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "nom d'utilisateur"
        self.fields['email'].widget.attrs['placeholder'] = "email"
        self.fields['password1'].widget.attrs['placeholder'] = "mot de passe"
        self.fields['password2'].widget.attrs['placeholder'] = "confirmation du mot de passe"
        for fieldname in ['username', 'email', 'password1', 'password2']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )

class LogInForm(AuthenticationForm):
    def __init__(self, request, *args, **kwargs):
        self.request = request
        super(AuthenticationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = "nom d'utilisateur"
        self.fields['password'].widget.attrs['placeholder'] = "mot de passe"
        for fieldname in ['username', 'password']:
            self.fields[fieldname].help_text = None
            self.fields[fieldname].label = ""

    class Meta:
        model = User
        fields = ('username', 'password', )