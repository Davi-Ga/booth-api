from django.shortcuts import render
from django.http import request
from .models import Booth

def home(request):


    context={

    }
    return render(request,'home.html',context=context)

def add_booth(request):
    context={

    }
    return render(request,'/add_booth.html',context=context)