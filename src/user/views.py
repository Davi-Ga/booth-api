from django.shortcuts import render
from forms import RegisterForm

def register(request):
    form=RegisterForm()
    
    try:
        form=RegisterForm(request.POST)
        

    except:
        print("error")