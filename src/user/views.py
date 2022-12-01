from django.shortcuts import render,redirect
from forms import RegisterForm

def register(request):
    form=RegisterForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
        try:
            form=RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('register')
            context={
                'form':form
            }
            return render(request,'register.html',context=context)

        except:
            print("error")