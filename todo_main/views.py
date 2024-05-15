from django.shortcuts import render
from todo.models import Task
from django.views.decorators.http import require_http_methods
import requests
@require_http_methods(["GET"])
def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('-updated_at')
    complted_tasks = Task.objects.filter(is_completed=True).order_by('-updated_at')
    response = requests.get('https://httpbin.org/ip')
    data = response.json()
    ip = data['origin']
    context = {
        'tasks' : tasks,
        'completed_tasks' :complted_tasks,
        'ip' : ip
    }
    return render(request, 'home.html', context)