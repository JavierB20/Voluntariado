
from django.contrib import admin
from django.urls import path
from tasks import views as task_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', task_views.task_list, name='task_list'),
    path('toggle/<int:pk>/', task_views.toggle_task, name='toggle_task'),
    path('delete/<int:pk>/', task_views.delete_task, name='delete_task'),
]