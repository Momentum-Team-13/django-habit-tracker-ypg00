from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint
from datetime import date

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
    goal = models.IntegerField()
    unit = models.CharField(max_length=255)
    user = models.ForeignKey('User', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Record(BaseModel):
    date = models.DateField(default=date.today)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    habit = models.ForeignKey('Habit', on_delete=models.CASCADE)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['habit', 'date'], name='unique_habit_date')
        ]
    
    def __str__(self):
        return f'{self.date}'