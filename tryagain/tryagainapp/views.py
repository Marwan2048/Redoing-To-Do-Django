from django.shortcuts import render ,redirect
from .forms import FormTask
from .models import Task
def homepage(request):
    task = Task.objects.filter(Task_completed = False)
    task = task.order_by("-Important")

    task = task[::-1]
    context = {"task" : task }
    return render(request,"main.html",context)

def add_task(request):
    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = FormTask()
    context = {"form":form}  
    return render(request, "add_task.html", context)


def completed_tasks(request):
    completed = Task.objects.filter(Task_completed =True)
    completed = completed[::-1]
    context = {"completed" : completed}
    return render(request,"completed_tasks.html",context)

def mark_as_done(request ,task_id):
    t_id = Task.objects.get(id=task_id)
    t_id.Task_completed = True
    t_id.save()
    return redirect("home")

def edit(request,task_id):
    t_id = Task.objects.get(id = task_id)
    form = FormTask(instance=t_id)
    if request.method == "POST":
        form = FormTask(request.POST,instance=t_id)
        if form.is_valid():
            form.save()
            return redirect("/")
    context = {"form":form}
    return render(request,"update_task.html",context)


def delete(request , task_id):
    t_id = Task.objects.get(id = task_id)
    t_id.delete()

def delete_completed_task(request,task_id):
    t_id = Task.objects.get(id = task_id)
    t_id.delete()
    return redirect("completed_tasks")

def remove_completed_tasks_all(request):
    task = Task.objects.filter(Task_completed =True)
    task.delete()
    return redirect("completed_tasks")

def confirmation(request):
    return render(request , "confirmation.html")