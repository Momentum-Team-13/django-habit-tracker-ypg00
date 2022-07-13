from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import User, Habit, Record

admin.site.register(User, UserAdmin)
admin.site.register(Habit)
admin.site.register(Record)