from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Server, Topic
from .forms import ServerForm

# Create your views here.

# servers = [
#     {'id' : 1 , 'name' : 'Servers Server'},
#     {'id' : 2 , 'name' : 'Anime'},
#     {'id' : 3 , 'name' : 'Music'},
    
# ]

def home(request):
    nam = request.GET.get('nam') if request.GET.get('nam') != None else ''

    servers = Server.objects.filter(
        Q(topic__name__icontains = nam) |
        Q(name__icontains = nam) |
        Q(description__icontains = nam) 
        ) #contains means case sensitive icontains means case INsensitive
    
    topics = Topic.objects.all()
    server_count = servers.count()
    context = {'servers' :servers, 'topics': topics, 'server_count' : server_count}
    return render(request, 'base/home.html' , context)

def server(request,sid):
    # for i in servers:
    #     if i['id'] == int(sid):
    #         server = i
    server = Server.objects.get(id=sid)

    context = {'server': server}
    return render(request, 'base/server.html' , context)

def createServer(request):
    form = ServerForm()

    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context = {'form' : form}
    return render(request , 'base/server_form.html', context)


def updateServer(request, pk):
    server = Server.objects.get(id=pk)
    form = ServerForm(instance=server)

    if request.method == "POST":
        form = ServerForm(request.POST, instance= server)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/server_form.html', context)

def deleteServer(request, pk):
    server = Server.objects.get(id=pk)

    if request.method == 'POST':
        server.delete()
        return redirect('home')

    return render(request, 'base/del.html',{'obj': server})