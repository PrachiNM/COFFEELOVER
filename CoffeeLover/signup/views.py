from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Users
import time

def signup(request):
    if request.method == 'POST':
        c_password = request.POST.get('c_password')
        password = request.POST.get('password')

        if password != c_password:
            messages.info(request, "Password Mismatch!!")
            # time.sleep(5)
            return render(request, "signup.html")
        else:
            firstname = request.POST.get('firstname')
            lastname = request.POST.get('lastname')
            emailid = request.POST.get('emailid')

        if User.objects.filter(email=emailid).exists():
            messages.info(request, "Email already taken")
            return redirect("signup")
        else:
            user = User.objects.create_user(username=emailid, email=emailid, first_name=firstname, last_name=lastname, password=password)
            user.save()
            messages.info(request, "User Created successfully")
            time.sleep(5)
            return redirect('thankyou')

    elif request.method == 'GET':
        return render(request, "signup.html")



def login(request):
    return render(request, 'login.html')


def thankyou(request):
    return render(request, 'thankyou.html')

def user_authentication(email, password):
    pass

