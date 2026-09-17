from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    completed = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)