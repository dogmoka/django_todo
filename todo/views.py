from django.shortcuts import render
from django.views.generic import ListView

from todo.models import TodoModel

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    # モデルの指定
    model = TodoModel