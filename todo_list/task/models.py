from django.db import models

# Create your models here.
class Task(models.Model):

    text = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)
    is_finished = models.BooleanField(default = False)
