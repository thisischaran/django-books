from django.contrib import admin
from . models import bookdetails,reviews,tag
# Register your models here.


admin.site.register(bookdetails)
admin.site.register(reviews)
admin.site.register(tag)