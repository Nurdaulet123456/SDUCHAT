from ast import Break
from email import message
from django.shortcuts import redirect, render
from django.http import HttpResponse 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import UserRegistraionsFroms, UserLoginForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required

def index(request):
    if request.method == 'POST':
        form = UserRegistraionsFroms(request.POST)
        email = request.POST['email']
        if form.is_valid():
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Error, because that is email is already in use')
            if "@stu.sdu.edu.kz" not in email:
                messages.error(request, 'Error')
            else:    
                messages.success(request, 'Account created')
                form.save()
                return redirect('sigin')
            
    else:
        form = UserRegistraionsFroms()
    return render(request, 'forms.html', {"form": form})



def sigIn(request):

    if request.method == "POST":
        form = UserLoginForms(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            
            return redirect('main')

            
        else:
            messages.success(request, 'Incorecct password or username')
            return redirect('sigin')
           
    else:
        form = UserLoginForms()
        

    context = {'form': form}
    return render(request, 'sigin.html', context)

def log_out(request):
    logout(request)
    return redirect('sigin')