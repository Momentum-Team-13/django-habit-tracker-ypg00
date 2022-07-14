from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Record

def home(request):
    return render(request, 'homepage.html')


