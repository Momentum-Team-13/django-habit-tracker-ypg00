from tkinter import CASCADE
from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(BaseModel):
    pass

    def __str__(self):
        return self.username

class Habit(BaseModel):
    name = models.CharField(max_length=255)
    goal = models.IntegerField(max_length=9)
    metric = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)

class Record(BaseModel):
    pass