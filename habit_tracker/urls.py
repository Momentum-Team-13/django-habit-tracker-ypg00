from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from habits import views as habits_views

urlpatterns = [
    path('', habits_views.home, name='homepage'),
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('auth/', include('registration.backends.simple.urls')),
]
