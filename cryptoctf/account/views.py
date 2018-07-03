from django.shortcuts import render,redirect, reverse 
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import userinfo
from django.http import HttpResponse

# Create your views here.
def signin(request, ):
    if request.method == 'GET':
        return render(request, 'account/signin.html', {})

    un = request.POST['un']
    pw = request.POST['pw']

    user = authenticate(request, username = un, password = pw)
    if user is not None:
        login(request, user)

    return redirect(reverse('index:index'))

def signup(request, ):
    if request.method == 'GET':
        return render(request, 'account/signup.html', {})

    un = request.POST['un']
    em = request.POST['em']
    ct = request.POST['ct']
    pw = request.POST['pw']
    
    try:
        user = userinfo.objects.create_user(un, em, pw, pt = 0, country = ct)
        user.save()
    except Exception as e:
        return HttpResponse('try a new uername plz.')

    user = authenticate(request, username = un, password = pw)
    if user is not None:
        login(request, user)
        print(user)

    return redirect(reverse('index:index'))

def signout(request, ):
    logout(request)
    return redirect(reverse('index:index'))