from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Message, Room
# Create your views here.

def roomForm(request):
    room = Room.objects.all()
    context = {
        'room': room
    }
    return render(request, 'roomForm.html', context)


def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    context = {
        'room' : room,
        'messages': messages
    }
    return render(request, 'room.html', context)