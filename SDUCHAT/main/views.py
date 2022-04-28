
from datetime import datetime
from typing import overload
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from forms.forms import UserRegistraionsFroms
from .models import People, Message
from .forms import MessageForm
from django.db.models import Q
from django.contrib.auth.models import User
# Create your views here.
@login_required(login_url='sigin')
def main(request):
    
    query = request.GET.get('searched') 
    if not query:
        query = ""
    people = People.objects.filter(Q(email__icontains=query), Q(username__icontains=query))
    
    if query == '':
        people = People.objects.all()

    users = User.objects.exclude(username=request.user.username)
    
    # Message 
    # emails = Message.objects.filter(to_user = request.user)
    # sysdate = datetime.now()
    # print(emails)
    # if request.method == 'POST':
    #     form = MessageForm()
    #     from_user = request.user
    #     to_user = request.POST['to_user']
    #     #subject = request.POST['subject']
    #     message = request.POST['message']
    #     mesa = Message(from_user=from_user, to_user=to_user,message=message)

    #     mesa.save()
    #     context = {
    #         'people': people,
    #         'form': form,
    #         'emails': emails,
    #         'from_user': from_user,
    #         'to_user': to_user,
    #         'sysdate': sysdate,
    #         'users': users
    #     }

    #     return redirect('main')
    # else: 
    #     form = MessageForm()

    context = { 
        'people': people,
        # 'form': form,
        # 'emails': emails,
        'users': users,
    }
    return render(request, 'main.html', context)


@login_required(login_url='sigin')
def mainarg(request, username):
    
    query = request.GET.get('searched') 
    if not query:
        query = ""
    people = People.objects.filter(Q(email__icontains=query), Q(username__icontains=query))
    
    if query == '':
        people = People.objects.all()

    users = User.objects.exclude(username=request.user.username)
    to_user = User.objects.get(username=username)
    
    # Message 
    # emails = Message.objects.filter(to_user = request.user)
    # sysdate = datetime.now()
    # print(emails)
    # if request.method == 'POST':
    #     form = MessageForm()
    #     from_user = request.user
    #     to_user = request.POST['to_user']
    #     #subject = request.POST['subject']
    #     message = request.POST['message']
    #     mesa = Message(from_user=from_user, to_user=to_user,message=message)

    #     mesa.save()
    #     context = {
    #         'people': people,
    #         'form': form,
    #         'emails': emails,
    #         'from_user': from_user,
    #         'to_user': to_user,
    #         'sysdate': sysdate,
    #         'users': users
    #     }

    #     return redirect('main')
    # else: 
    #     form = MessageForm()



    context = { 
        'people': people,
        # 'form': form,
        # 'emails': emails,
        'users': users,
        'username': username,
        'to_user': to_user.username,
        'pk': to_user.pk,
    }
    return render(request, 'main.html', context)

# def filterUser(request, email):
#     user = People.objects.filter(Q(email__icontains=email))
#     return render(request, "main.html", {"user": user})
    

   