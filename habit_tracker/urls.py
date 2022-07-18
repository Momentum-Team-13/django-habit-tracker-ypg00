from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from habits import views as habits_views

urlpatterns = [
    path('', habits_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('auth/', include('registration.backends.simple.urls')),

    # Habits
    path('habits/', habits_views.list_habits, name='list_habits'),
    # path('habits/<int:pk>/', habits_views.habit_detail, name='habit_detail'),
    path('habits/add/', habits_views.add_habit, name='add_habit'),
    # path('habits/delete/', habits_views.delete_habit, name='delete_habit'),

    # Records
    # path('records/', habits_views.list_records, name='list_records'),
    # path('records/<int:pk>/', habits_views.record_detail, name='record_detail'),
    # path('records/add/', habits_views.record_detail, name='record_detail'),
]
