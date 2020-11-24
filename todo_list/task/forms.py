from django import forms

from .models import Task

class TaskForm(forms.ModelForm):
    """
    Extract new information on task to add
    """
    class Meta:
        model = Task
        fields = {
            'text',
            #'date',
            'is_finished'
        }
