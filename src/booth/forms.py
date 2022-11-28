from django.forms import ModelForm
from .models import Booth
from django import forms

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Booth
        fields = ['username','email','password']
        