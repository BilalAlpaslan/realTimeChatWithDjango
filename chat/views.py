from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Room,Message

def index(request):
    context={
        "users": User.objects.all()
    }
    return render(request, 'index.html', context)

def room(request, room_name):
    a,b=room_name.split("0")  
    room, created = Room.objects.get_or_create(slug=room_name)

    context={
        "room_name": room_name,
        "room": room
    }
    
    if request.user.username == a or request.user.username == b:
        return render(request, 'room.html', context)
    else:
        return redirect(index)

def msg(request,room_name,message):
    room =Room.objects.get(slug=room_name)
    a = Message.objects.create(room=room,author=request.user,content=message)
    print(a,request.user,room_name,message)
    return a