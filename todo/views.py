from django.shortcuts import render
from django.views.generic import ListView, DetailView

from todo.models import TodoModel

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    # モデルの指定
    model = TodoModel

# DetailViewはリストの中から任意の一つを選んで詳細を表示する
# 何を表示するか明示する必要がある　URLにidを含める必要がある
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel