from django.shortcuts import render, redirect
from .forms import userform, profileform
from django.http import HttpResponse
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib import messages
#from .models import userprofile, skills
# Create your views here.

def userprofileshow(request):
       # print("i have come inside")
       # print(request.user.userprofile.id)
        #id1 = request.user.userprofile.id
        #profile =  userprofile.objects.get(id = id1 )
        profile = request.user.userprofile
        skill = profile.skills_set.all()
        form =  profileform(instance=request.user.userprofile)
        print(skill)
        context = {"form":form,"skills":skill}
        return render(request,'users/userprofile.html',context)

def loginuser(request):
    form = AuthenticationForm()
    context ={"form": form,"login":"login"}
    if request.user.is_authenticated:
        return redirect ('userprofileshow')
    if request.method =="POST":
        form =AuthenticationForm(request.POST)
        user1 = User.objects.get(username= request.POST["username"])
        if user1:
            valid = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if valid is not None:
                messages.success(request,"welcome user ")
                login(request,  valid)
                return redirect ('userprofileshow')
            else:
                messages.error(request,"invalid credentials")
                context ={"form": form,"login":"login"}
                return render(request,'users/users.html',context)
        else:
            print("user not found")
        return render(request,'users/users.html')
    return render(request,'users/users.html',context)


def registeruser(request):
    form = UserCreationForm()
    context ={"form": form}
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user registerd sucessfully ")
            return render(request,'users/users.html')
    return render(request,'users/users.html',context)


def logoutuser(request):
    logout(request)
    return redirect(loginuser)

    