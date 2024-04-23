from django.shortcuts import render
from .models import Server

# Create your views here.

# servers = [
#     {'id' : 1 , 'name' : 'Servers Server'},
#     {'id' : 2 , 'name' : 'Anime'},
#     {'id' : 3 , 'name' : 'Music'},
    
# ]

def home(request):
    servers = Server.objects.all()
    context = {'servers' :servers}
    return render(request, 'base/home.html' , context)

def server(request,sid):
    # for i in servers:
    #     if i['id'] == int(sid):
    #         server = i
    server = Server.objects.get(id=sid)

    context = {'server': server}
    return render(request, 'base/server.html' , context)