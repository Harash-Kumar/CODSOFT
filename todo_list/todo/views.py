from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def index(request):
    tasks = Task.objects.exclude(status="deleted").order_by("-id")
    return render(request, "todo/index.html", {"tasks": tasks})

def add_task(request):
    if request.method == "POST":
        text = request.POST.get("task")
        if text:
            Task.objects.create(text=text)
    return redirect("index")

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = "completed" if task.status != "completed" else "active"
    task.save()
    return redirect("index")

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.status = "deleted"
    task.save()
    return redirect("index")

def history(request):
    filter_type = request.GET.get("filter", "all")

    if filter_type == "completed":
        completed_tasks = Task.objects.filter(status="completed").order_by("-updated_at")
        deleted_tasks = []
    elif filter_type == "deleted":
        completed_tasks = []
        deleted_tasks = Task.objects.filter(status="deleted").order_by("-updated_at")
    else:
        completed_tasks = Task.objects.filter(status="completed").order_by("-updated_at")
        deleted_tasks = Task.objects.filter(status="deleted").order_by("-updated_at")

    return render(request, "todo/history.html", {
        "completed": completed_tasks,
        "deleted": deleted_tasks,
        "filter_type": filter_type
    })
