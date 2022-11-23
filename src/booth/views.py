from django.shortcuts import render
from django.http import request
from models import Booth,User

def home(request):
    Booth.object.all()

    context={

    }
    return render(request,'/home.html',context=context)