from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

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

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    # 作成成功後のリダイレクト先URL
    # reverse_lazy を使う理由は、クラス定義時にURLを遅延評価（＝必要になるまで解決しない）するため
    success_url = reverse_lazy('list') 

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    fields = ('title', 'memo', 'priority', 'duedate')
    success_url = reverse_lazy('list')
