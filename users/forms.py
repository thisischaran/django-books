from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import userprofile

class userform(ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class profileform(ModelForm):
    class Meta:
        model = userprofile
        fields = '__all__'

