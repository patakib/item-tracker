from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import transaction



from .models import *
from .forms import *

# Create your views here.

def index(request):
    tasks = Task.objects.all().order_by('deadline')
    context = {'tasks': tasks}
    return render(request, 'trackerapp/list.html', context)

@transaction.atomic()
def editItem(request, pk):
    task = Task.objects.select_for_update().get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'trackerapp/edit_item.html', context)


def deleteItem(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item':item}
    return render(request, 'trackerapp/delete.html', context)


def newItem(request):
    form = TaskForm()
    task = form.instance

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form':form}
    return render(request, 'trackerapp/new_item.html', context)
