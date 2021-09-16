from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
from django.contrib import messages


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