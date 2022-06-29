from django.http import HttpRequest, JsonResponse
from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
#from .forms import CustomerForm



def admin(request):
    return render(request, 'admin')


def index(request):
    return render(request, 'core/index.html')


def receptionFL(request):
    return render(request, 'core/receptionFL.html')


def receptionUL(request):
    return render(request, 'core/receptionUL.html')


def applicant(request):
    return render(request, 'core/applicant.html')


def cards(request):
    return render(request, 'core/cards.html')


def task_status(request):
    return render(request, 'core/task_status.html')


def executor(request):
     return render(request, 'core/executor.html')


def report(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'core/report.html', {'title': 'Главная страница из views.py', 'tasks': tasks})


def waiting(request):
    return render(request, 'core/waiting.html')


def connection(request):
    return render(request, 'core/connection.html')


def addTask(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/report')
        else:
            error = 'ФОРМА НЕ ВЕРНАЯ!!!'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'core/tasks_plus.html', context)