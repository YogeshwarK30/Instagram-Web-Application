from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate, login, logout, get_user_model

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        return redirect("/explore/")
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request,user)
            return redirect("/explore/")
        else:
            print("Login Failed")
    return render(request,'index.html')


def signup(request):
    if request.method == "POST":
        print("Request Post")
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone')
        bio = request.POST.get('bio')
        print(username)
        user_obj = User.objects.create(username=username, first_name=name, email=email)
        user_obj.set_password(password)
        user_obj.save()
        user_info_obj = UserInfo.objects.create(phone_number=phone_number, bio=bio, user=user_obj)
        user = authenticate(username=username, password=password)
        login(request,user)
        return redirect("/explore/")
    return render(request,'signup.html')





def test(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        name = request.POST.get('name')
        email = request.POST.get('email')
        obj = User.objects.create(username=username, first_name=name, email=email)
        obj.set_password(password)
        obj.save()
        print(obj)
        pass
    return render(request,'test.html')



def user_logout(request):
    logout(request)
    return redirect("/")