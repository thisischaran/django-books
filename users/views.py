from django.shortcuts import render

# Create your views here.



def userhomepage(request):
    return render(request,'users/users.html')