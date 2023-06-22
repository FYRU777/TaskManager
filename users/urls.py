from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name="home"),
    path("signup/", views.SignUp.as_view(), name="signup"),
    path('add_task/', views.add_task, name='add_task'),
    path('done/', views.done, name='done'),
    path('tasks/', views.show_all_tasks, name='tasks'),
    path('task/<int:task_id>/', views.show_one_task, name='one_task')
]
