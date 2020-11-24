from django.shortcuts import render
from .models import Task

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
