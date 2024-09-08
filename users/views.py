from django.shortcuts import render
from .forms import userform
from django.http import HttpResponse
from django.contrib.auth.forms  import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.



def loginuser(request):

    form = AuthenticationForm()
    context ={"form": form,"login":"login"}

    if request.method =="POST":
        form =AuthenticationForm(request.POST)
        user1 = User.objects.get(username= request.POST["username"])
        if user1:
            valid = authenticate(request, username=request.POST["username"], password=request.POST["password"])
            if valid is not None:
                messages.success(request,"welcome user ")
                login(request,  valid)
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