from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

app_name = "task"

# Create your views here.
def homepage_view(request):
    """
    Home page of application
    """
    # get all tasks
    queryset = Task.objects.all()
    context = {
        'task_list' : queryset
    }

    return render(request, "homepage.html", context)

def add_task_view(request):
    """
    Add a new task to DB
    """
    
    # read POST request from homepage
    if request.POST:
        task_to_add = request.POST["task"]

    # get date

    # add to database
    task = Task(text = task_to_add, 
                is_finished = False)

    # save to DB
    task.save()

    # redirect to main page
    return HttpResponseRedirect(reverse("task:homepage"))

def finished_task_view(request):
    """
    Mark a task as finished in the DB
    """
    #return render(request)
    pass

def edit_task_view(request):
    """
    Edit the text of a task
    """
    pass

def delete_task_view(request):
    """
    Mark a task as deleted
    """
    pass
