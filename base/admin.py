from django.contrib import admin

# Register your models here.

from .models import Server, Topic, Msg, User

admin.site.register(Server)
admin.site.register(Topic)
admin.site.register(Msg)
admin.site.register(User)