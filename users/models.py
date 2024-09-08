from django.db import models
from django.contrib.auth.models import User
from uuid import uuid4
# Create your models here.


class userprofile(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    user = models.OneToOneField(User, null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    location = models.CharField(max_length=200, blank=True, null=True, default="Earth")
    short_intro = models.CharField(max_length=200, blank=True, null=True, default="This is a default bio. User has not added a bio yet.")
    bio = models.TextField(blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_youtube = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username


class skills(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    created_date = models.DateTimeField(auto_now_add=True, editable=False)
    owner = models.ForeignKey(userprofile,null=True,blank=True, on_delete= models.CASCADE)
    name = models.CharField(max_length=100, null=True, editable=True)
    def __str__(self):
        return self.name

