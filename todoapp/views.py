from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required



# Create your views here.


def home(request):
    tasks = Task.objects.all()
    context={'tasks':tasks}
    return render(request,'index.html',context)

def createTask(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            todo=form.cleaned_data.get('name')
            
            messages.success(request,'Account was created for'+todo)
            return render(request, 'login.html', {'form': TaskForm(request.GET)})
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

def DeleteTask(request,pk):
    task=Task.objects.get(id=pk)
    if request.method=='POST':
        task.delete()
        return redirect('/')
    context={'item':task}
    return render(request,'delete.html',context)

def UpdateTask(request,pk):
    task=Task.objects.get(id=pk)
    form=TaskForm(instance=task)
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'create_task.html',context)


def signup(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')    
            return redirect('login')
    else:
        form = UserRegisterForm()

    context = {'form': form}
    return render(request, 'signup.html', context)


def user_login(request):
    if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

    context = {}
    return render(request, 'login.html', context)

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')
