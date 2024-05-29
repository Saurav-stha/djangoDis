from django.db import models
# from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True)
    bio = models.TextField(null=True)

    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=220)

    def __str__(self):
        return self.name

class Server(models.Model):
    owner = models.ForeignKey(User, on_delete=models.SET_NULL,null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True , blank=True) # null for db and blank for frontend
    members = models.ManyToManyField(User, related_name='members', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name
    

class Msg(models.Model): # Msg written cause message is keyword in django
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated', '-created']


    def __str__(self):
        return self.body[0:40]
    