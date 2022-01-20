from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
import time

def signup(request):
    return render(request, "signup.html")


def register_user(request):
    password = request.POST['password']
    c_password = request.POST['c_password']

    if password != c_password:
        messages.info(request, "Password Mismatch!!")
        time.sleep(5)
        return redirect('signup')
    else:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        emailid = request.POST['emailid']

        if User.objects.filter(email=emailid).exists:
            messages.info(request, "Email already taken")
            return redirect('register_user')
        else:
            user = User.objects.create_user(email=emailid, firstname=firstname, lastname=lastname, password=password)
            user.save()
            messages.info(request, "User Created successfully")
            time.sleep(5)
        return redirect('thankyou')
        


def login(request):
    return render(request, 'login.html')


def thankyou(request):
    return render(request, "thankyou.html")

def user_authentication(email, password):
    pass

