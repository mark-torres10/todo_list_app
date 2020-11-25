from django.shortcuts import render
from .models import Task
from .forms import TaskForm

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
    Add a new task
    """
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = TaskForm()

    context = {
        'form' : form
    }

    #return render(request, "create_entry.html", context)
    #return an HTTP request instead: https://docs.djangoproject.com/en/3.1/ref/request-response/
    # keeps you on the page that you're on, since it's just an HTTP request to do CRUD
    # serializers turn db --> json, render to site
    # 1) return HTTP request, not view
    # 2)
    # use VSCode

def finished_task_view(request):
    """
    Mark a task as finished
    """
    #return render(request)
    pass

def cancelled_task_view(request):
    """
    Mark a task as cancelled
    """
    pass

def delete_task_view(request):
    """
    Mark a task as deleted
    """
    pass
