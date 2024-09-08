from django.shortcuts import render
from .models import bookdetails



# Create your views here.


def bookhomepage(request):
    booklist = bookdetails.objects.all()
    context = {"books":booklist}
    return render(request,'books/books.html',context)
