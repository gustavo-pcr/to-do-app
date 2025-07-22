from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('update_task/<task_id>', views.updateTask, name='updateTask'),
    path('delete_task/<task_id>', views.deleteTask, name='deleteTask'),
]
