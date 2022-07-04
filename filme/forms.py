from django.contrib.auth.forms import UserCreationForm
from .models import Usuario
from django import forms

class FormHomePage(forms.Form):
    email = forms.EmailField(label = False)

class CriarContaForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2')