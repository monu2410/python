from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Task
from django.views.decorators.http import require_POST,require_http_methods,require_GET
# Create your views here.
@require_POST
def add_task(request):
    task = request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')

@require_GET
def mark_as_done(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')

@require_GET
def mark_as_undone(request,pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = False
    task.save()
    return redirect('home')

@require_GET
def edit_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    context = {
        'get_task' : task,
    }
    return render(request , 'edit_task.html',context)
@require_POST
def update_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.task = request.POST.get('task', '')
    task.save()  
    context = {
        'get_task' : task,
    }
    return render(request , 'edit_task.html',context)
@require_GET
def delete_task(request,pk):
    task = get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')