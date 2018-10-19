from django.shortcuts import render,redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login as user_login,authenticate,logout as user_logout
from django.contrib import messages

# Create your views here.

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        newUser = User(username = username)
        newUser.set_password(password)
        newUser.save()
        user_login(request,newUser)
        messages.success(request,"Başarıyla Kayıt Oldunuz...")

        return redirect("index")
    context = {
        "form" : form
    }
    return render(request,"register.html",context)

    
def login(request):
    form = LoginForm(request.POST or None)
    
    context = {
        "form" : form
    }

    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username = username,password = password)
        if user is None:
            messages.error(request,"Kullanıcı Adı veya Parola Yanlış!")
            return render(request,"login.html",context)

        user_login(request,user)
        messages.success(request,"Başarıyla Giriş Yaptınız.")
        return redirect("index")
        

    return render(request,"login.html",context)

def logout(request):
    user_logout(request)
    messages.success(request,"Başarılı bir şekilde çıkış yaptınız.")
    return redirect("index")  