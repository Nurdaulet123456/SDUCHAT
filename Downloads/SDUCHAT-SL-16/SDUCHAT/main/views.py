from datetime import datetime
from typing import overload
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from forms.forms import UserRegistraionsFroms
from .models import People, ChatModel
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from myProfile.models import Profile


User = get_user_model()
# Create your views here.

def index(request):
    users = User.objects.all()
    if request.method == 'POST':
        query = request.POST.get('searched') 
        users =  users = User.objects.filter(username__icontains=query)
        
        
    # users = User.objects.exclude(username=request.user.username)
    
    # print('sdfsdf',query)
    return render(request, 'index.html', context={'users': users})



def izbrannyie(request):
    if request.method=="POST":
        val = request.POST.get('id')
        star_us = Profile.objects.get(pk=val)
        if star_us in request.user.profile.star_user.all():
            request.user.profile.star_user.remove(star_us)
        else:
            request.user.profile.star_user.add(star_us)
    
    return render(request, 'starred.html') 




def main(request, username):
    query = request.POST.get('searched') 
    users = User.objects.all()
    user_obj = User.objects.get(username=username)
    # users = User.objects.exclude(username=request.user.username)

    if not query:
        query = ""

    if query:
        users = User.objects.filter(Q(username__icontains=query))
        print(users)
    else:
        users = User.objects.all()
 
   
        

    

    if request.user.id > user_obj.id:
        thread_name = f'chat_{request.user.id}-{user_obj.id}'
    else:
        thread_name = f'chat_{user_obj.id}-{request.user.id}'
    message_objs = ChatModel.objects.filter(thread_name=thread_name)

    # message = ChatModel.objects.filte)

    
    return render(request, 'main.html', context={'user': user_obj, 'users': users, 'messages': message_objs})


def starred_users(request):
    if request.method=="POST":
        val = request.POST.get('id')
        star_us = Profile.objects.get(pk=val)
        if star_us in request.user.profile.star_user.all():
            request.user.profile.star_user.remove(star_us)
        else:
            request.user.profile.star_user.add(star_us)
    
    return redirect('main')


    