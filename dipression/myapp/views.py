from django.db.models import Q
from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate, logout, login
from .models import *
import random
# Create your views here.

def index(request):
    return render(request, 'index.html')

def login(request):
    error = ""
    if request.method == 'POST':
        e = request.POST['emailid']
        p = request.POST['password']
        user = authenticate(username=e, password=p)
        try:
            if user is not None:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "no"
    return render(request, 'login.html', locals())

def register(request):
    error = ""
    if request.method == "POST":
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        emailid = request.POST['emailid']
        Password = request.POST['password']
        mobileNumber = request.POST['mobileNumber']

        try:
            user = User.objects.create_user(username=emailid, password=Password, first_name=firstName, last_name=lastName)
            Signup.objects.create(user=user, mobileNumber=mobileNumber)
            error = "no"
        except:
            error = "yes"
    return render(request, 'register.html', locals())

def test(request):
    if request.method == "POST":

        a = [1,2,3,4]
        random_num = random.choice(a)
        
        if random_num == 1:
            return render(request, 'decision/decision1.html', locals())
        elif random_num == 2:
            return render(request, 'decision/decision2.html', locals())
        elif random_num == 3:
            return render(request, 'decision/decision3.html', locals())
        elif random_num == 4:
            return render(request, 'decision/decision4.html', locals())
        
    return render(request, 'test.html', locals())



def decision1(request):
    return render(request, 'decision/decision1.html')

def decision2(request):
    return render(request, 'decision/decision2.html')

def decision3(request):
    return render(request, 'decision/decision3.html')

def decision4(request):
    return render(request, 'decision/decision4.html')