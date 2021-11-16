from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *

def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'home', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("first")
        else:
            error = 'NOT RIGHT'


    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


def vk(request):
    return render(request, 'main/vk.html')


def nenad(request):
    if request.method == 'POST':
        form = nenad(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = nenad()
    return render(request, 'nenad.html', {'form': form})



