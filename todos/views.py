from django.shortcuts import render
from django.http import HttpResponse

def todo_list(request):
  nome="Cleyson"
  alunos=["Elton Fonseca" ,"Ariel Sardina" ]
  return render(request,"todos/todo_list.html", {"nome":nome, "alunos":alunos})
