from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    # Crear nueva tarea (POST)
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        if title:
            Task.objects.create(title=title)
            return redirect('task_list')

    tasks = Task.objects.order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

def toggle_task(request, pk: int):
    t = get_object_or_404(Task, pk=pk)
    t.done = not t.done
    t.save()
    return redirect('task_list')

def delete_task(request, pk: int):
    t = get_object_or_404(Task, pk=pk)
    t.delete()
    return redirect('task_list')
