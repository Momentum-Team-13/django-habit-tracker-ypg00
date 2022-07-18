from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import User, Habit, Record
from .forms import HabitForm

def home(request):
    if request.user.is_authenticated:
        return redirect('list_habits')
    return render(request, 'home.html')

@login_required
def list_habits(request):
    habits = Habit.objects.filter(user=request.user.pk)
    return render(
        request, 'habits/list_habits.html', 
        {'user': request.user, 'habits': habits})
        
@login_required
def add_habit(request):
    if request.method == 'POST':
        form = HabitForm(data=request.POST)
        if form.is_valid():
            habit = form.save(commit=False)
            habit.user = request.user
            habit.save()
            return redirect('list_habits')
    else:
        form = HabitForm()
    return render(request, 'habits/add_habit.html', {'form': form})

@login_required
def habit_detail(request, pk):
    habit = Habit.objects.filter(user=request.user.pk).get(pk=pk)
    return render(request, 'habits/habit_detail.html', {'habit': habit})

