from django.shortcuts import render, redirect
from .models import CustomUser
from django.contrib.auth.models import auth
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.


def register(request):
    if request.method == 'POST':
        name = request.POST['Name']
        contact = request.POST['contact']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if CustomUser.objects.filter(email=email).exists():
                return redirect('register')
            else:
                user=CustomUser.objects.create_user(name=name,contact_num=contact,email=email,password=password1)
                user.save()
                return redirect('login')
        else:
            return redirect('register')
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method =='POST':
        email=request.POST['email']
        password=request.POST['password']
        user=auth.authenticate(email=email,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/utilities/home')
        else:
            return redirect('login')
    else:
        return render(request, 'signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
