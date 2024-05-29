from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Server, User


class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name','username', 'email', 'password1', 'password2','avatar','bio']


class ServerForm(ModelForm):
    class Meta:
        model = Server
        fields = '__all__'
        exclude = ['owner','members']


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','username','email','avatar','bio']
