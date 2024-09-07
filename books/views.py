from django.shortcuts import render

# Create your views here.


def bookhomepage(request):
    return render(request,'books/books.html')