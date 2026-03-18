from django.urls import path 
from . import views
urlpatterns = [
    path("" , views.homepage , name="home"),
    path("add_task/" , views.add_task , name="add_task"),
    path("completed_tasks/" , views.completed_tasks , name ="completed_tasks"),
    path("<int:task_id>" , views.mark_as_done , name="mark_as_done"),
    path("<int:task_id>" , views.delete , name="delete"),
    path("completed_tasks/<int:task_id>" , views.delete_completed_task , name="completed_delete"),
    path("update_task/<int:task_id>" , views.edit , name="edit"),
    path("completed_tasks/confirmation/" , views.confirmation , name="confirmation"),
    path("remove_all/" , views.remove_completed_tasks_all , name="remove_all"),
]