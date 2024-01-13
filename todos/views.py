from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Todo

class TodoListView(ListView):
  model=Todo

class TodoCreateViws(CreateView):
  model = Todo
  fields=["title", "deadline"]
  success_url=reverse_lazy("todo_list")

class TodoUpdateView(UpdateView):
  model=Todo
  fields=["title", "deadline"]
  success_url=reverse_lazy("todo_list")
  
class TodoDeleteView(DeleteView):
  model=Todo
  