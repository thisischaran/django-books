from django.db import models
from uuid import uuid4
from users.models import userprofile

# Create your models here.
class bookdetails(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    createddate = models.DateTimeField(auto_now_add=True, editable=False)
    title = models.CharField(max_length=200, editable=True, null=True)
    description  = models.TextField(null=True, editable=True)
    owner = models.ForeignKey(userprofile,on_delete=models.CASCADE, null=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    def __str__(self):
        return self.title
    
class reviews(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    createddate = models.DateTimeField(auto_now_add=True, editable=False)
    owner = models.ForeignKey(userprofile, on_delete= models.CASCADE,null=True)
    description = models.TextField(null=True,editable=True)
    bookname = models.ForeignKey(bookdetails,on_delete=models.SET_NULL,editable=True,blank=True,null=True)
    VOTE_LOGIC = (('up','Up Vote'),('Down','Down vote'))
    value = models.CharField(max_length=100,choices=VOTE_LOGIC,null=True,blank=True,editable=True)
    def __str__(self):
        return self.value
    
class tag(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    createddate = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(max_length=100, editable=True,blank=True, null=True)
    def __str__(self):
        return self.name








