from datetime import date
from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView,View
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Todo
from django.shortcuts import get_object_or_404,redirect
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
  success_url=reverse_lazy("todo_list")
  
  
class TodoCompleteView(View):
  def get(Self,request,pk):
    todo=get_object_or_404(Todo, pk=pk)
    todo.mark_has_complete()
    return redirect("todo_list")