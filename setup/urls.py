
from django.contrib import admin
from django.urls import path
from todos.views import TodoListView,TodoCreateViws
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TodoListView.as_view(), name="todo_list"),
    path("create",TodoCreateViws.as_view(),name="todo_create"),
    ]
