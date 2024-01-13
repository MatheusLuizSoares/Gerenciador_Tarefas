from django.shortcuts import render
from django.views.generic import ListView
from django.http import HttpResponse
from .models import Todo

class TodoListView(ListView):
  model=Todo