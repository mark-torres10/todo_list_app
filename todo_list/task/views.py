from django.shortcuts import render
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse, HttpResponseRedirect, Http404
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

def modify_task_view(request):
    """
    Modify an existing task (mark as finished, delete it, or edit it)
    """

    if request.POST:
        type_of_change = request.POST['change_type']
        task_id = request.POST["task-id"]

    print(f"The task id we want to manipulate is: {task_id} and the type of change is: {type_of_change}")
    print(request.POST)

    try:
        task = Task.objects.get(pk=task_id)
    except Task.DoesNotExist:
        raise Http404("Task doesn't exist.")

    if type_of_change == "finish":
        updateForm=TaskForm(instance=item)
    elif type_of_change == "edit":
        pass
    elif type_of_change == "delete":
        Task.objects.filter(id=task_id).delete()
        return HttpResponseRedirect(reverse("task:homepage"))


    return HttpResponse("Finished editing!")