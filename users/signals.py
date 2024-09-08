from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import  userprofile
from django.contrib.auth.models import User
from .models import userprofile


@receiver(post_save, sender = User)
def createuserprofile(sender, instance, created, **kwargs):
    if created:
        print("usercreated")
        user1 = instance
        profile = userprofile.objects.create(
        user = user1,
        name = user1.first_name,
        username = user1.username

            )
    
@receiver(post_delete, sender =userprofile)
def deleteuserprofile(sender, instance,  **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass


