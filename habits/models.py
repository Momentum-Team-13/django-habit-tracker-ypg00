from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint

class BaseModel(models.Model):
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class User(AbstractUser):

    def __str__(self):
        return self.username

class Habit(BaseModel):
    name = models.CharField(max_length=255)
    goal = models.IntegerField(default=0, null=True, blank=True)
    unit = models.CharField(max_length=255, null=True, blank=True)
    creator = models.ForeignKey('User', on_delete=models.SET_NULL, null=True, blank=True)

class Record(BaseModel):
    date = models.DateField()
    quantity = models.IntegerField(default=0, null=True, blank=True)
    habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_habit_date')
        ]