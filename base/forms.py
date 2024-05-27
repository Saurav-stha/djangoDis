from django.forms import ModelForm
from .models import Server
from django.contrib.auth.models import User

class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = '__all__'
        exclude = ['owner','members']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','email']
