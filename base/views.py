from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from .models import Server, Topic, Msg
from .forms import ServerForm

# Create your views here.

# servers = [
#     {'id' : 1 , 'name' : 'Servers Server'},
#     {'id' : 2 , 'name' : 'Anime'},
#     {'id' : 3 , 'name' : 'Music'},
    
# ]

def loginPage(request):

    page = 'login'

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username Or Password is invalid')

        

    context = {'page': page}
    return render(request, 'base/login_register.html',context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    # page = 'register'
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Error aao register garda')


    return render(request, 'base/login_register.html', {'form': form})


def home(request):
    nam = request.GET.get('nam') if request.GET.get('nam') != None else ''

    servers = Server.objects.filter(
        Q(topic__name__icontains = nam) |
        Q(name__icontains = nam) |
        Q(description__icontains = nam) 
        ) #contains means case sensitive icontains means case INsensitive
    
    topics = Topic.objects.all()
    server_count = servers.count()
    server_msgs = Msg.objects.filter(Q(server__topic__name__icontains = nam))
    context = {'servers' :servers, 'topics': topics, 'server_count' : server_count, 'server_msgs':server_msgs}
    return render(request, 'base/home.html' , context)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    servers = user.server_set.all()
    topics = Topic.objects.all()
    server_msgs = user.msg_set.all()
    server_count = Server.objects.all().count()
    context = {'user':user,'servers':servers, 'topics': topics, 'server_msgs': server_msgs,'server_count': server_count}
    return render (request, 'base/profile.html', context)

def server(request,sid):
    # for i in servers:
    #     if i['id'] == int(sid):
    #         server = i
    server = Server.objects.get(id=sid)

    msgs = server.msg_set.all() # msg is the Msg class in models.py and _set means calling set function of msg class

    members = server.members.all()
    if request.method == "POST":
        msg = Msg.objects.create(
            user = request.user,
            server = server,
            body = request.POST.get('body')    
        )
        # server.members.add(request.user)
        return redirect('server', sid = server.id)

    context = {'server': server, 'msgs': msgs, 'members': members}
    return render(request, 'base/server.html' , context)


@login_required(login_url='login')
def createServer(request):
    form = ServerForm()
    topics = Topic.objects.all()

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)

        Server.objects.create(
            owner = request.user,
            topic= topic,
            name = request.POST.get('server_name'),
            description = request.POST.get('server_description')
        )
        return redirect('home')
        
    context = {'form' : form, 'topics': topics}
    return render(request , 'base/server_form.html', context)


@login_required(login_url='login')
def updateServer(request, pk):
    server = Server.objects.get(id=pk)
    form = ServerForm(instance=server)
    topics = Topic.objects.all()

    if request.user != server.owner:
        return HttpResponse('Not authorized!')

    if request.method == "POST":
        form = ServerForm(request.POST, instance= server)

        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form, 'topics':topics, 'server': server}
    return render(request, 'base/server_form.html', context)


@login_required(login_url='login')
def deleteServer(request, pk):
    server = Server.objects.get(id=pk)

    if request.user != server.owner:
        return HttpResponse('Not authorized!')

    if request.method == 'POST':
        server.delete()
        return redirect('home')

    return render(request, 'base/del.html',{'obj': server})


@login_required(login_url='login')
def joinServer(request, pk,):
    server = Server.objects.get(id=pk)
    
    if request.user in server.members.all():
        return HttpResponse("You are already a member of this server.")# already checked in the file
    
    server.members.add(request.user)
    server.save()
    return redirect('server', sid = server.id)

login_required(login_url='login')
def leaveServer(request, pk):
    server = Server.objects.get(id=pk)
    
    if request.user in server.members.all():
        server.members.remove(request.user)
        server.save()
    else:
        return HttpResponse("You are not a member of this server.") # already checked in the file
    
    return redirect('server', sid = server.id)

@login_required(login_url='login')
def deleteMsg(request, pk):
    msg = Msg.objects.get(id=pk)
    # server = Server.objects.get(id=pk)

    if request.user != msg.user:
        return HttpResponse('Not authorized!')

    if request.method == 'POST':
        msg.delete()
        # return redirect('server', sid = server.id)
        return redirect('home')

    return render(request, 'base/del.html',{'obj': msg})


