from django.shortcuts import render

# Create your views here.

servers = [
    {'id' : 1 , 'name' : 'Servers Server'},
    {'id' : 2 , 'name' : 'Anime'},
    {'id' : 3 , 'name' : 'Music'},
    
]

def home(request):
    context = {'servers' :servers}
    return render(request, 'base/home.html' , context)

def server(request,sid):
    for i in servers:
        if i['id'] == int(sid):
            server = i

    context = {'server': server}
    return render(request, 'base/server.html' , context)