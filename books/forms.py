from django.forms import ModelForm
from .models import bookdetails

class bookform(ModelForm):
    class Meta:
        model = bookdetails
        fields = '__all__'