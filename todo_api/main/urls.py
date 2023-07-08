from django.urls import path
from .views import task_list, task_detail, task_create, task_delete


urlpatterns = [
    path('tasks/', task_list ),
    path('tasks/int:pk', task_detali),
    path('task_create/', task_create),
    path('task_delete/int:pk', task_delete)

]