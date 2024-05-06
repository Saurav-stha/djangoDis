from django.forms import ModelForm
from .models import Server

class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = '__all__'
        exclude = ['owner','members']
