from django.urls import path
from taskweb import views

urlpatterns=[
    path("signup",views.SignUpView.as_view(),name="register"),
    path("login",views.LoginView.as_view(),name="sign-in"),
    path("home",views.IndexView.as_view(),name="home"),
    path("todos/add",views.TaskCreateView.as_view(),name="task-add"),
    path("tasks/all",views.TaskListView.as_view(),name="task-all"),
    path("task/detail/<int:id>",views.TaskDetailView.as_view(),name="task-detail"),
    path("task/remove/<int:id>",views.TaskDeleteView.as_view(),name="task-delete"),
    path("task/change/<int:id>",views.TaskEditView.as_view(),name="task-edit"),
    path("signout",views.LogOutView.as_view(),name="sign-out") 
]
