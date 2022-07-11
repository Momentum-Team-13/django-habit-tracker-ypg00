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
    goal = models.IntegerField(max_length=9, null=True, blank=True)
    metric = models.CharField(max_length=255, null=True, blank=True)
    user = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)

class Record(BaseModel):
    quantity = models.IntegerField(max_length=9, null=True, blank=True)
    date = models.DateField(max_length=255, null=True, blank=True)
    habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, null=True, blank=True)