from django.shortcuts import render

def mainpageview(request):
    return render(request,'main.html')