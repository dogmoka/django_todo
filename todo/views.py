from django.shortcuts import redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from todo.forms import TodoForm
from todo.models import TodoModel
from django.db.models import Case, When, IntegerField, Value

# Create your views here.

class TodoList(ListView):
    template_name = 'list.html'
    # モデルの指定
    model = TodoModel
    
    # ビューが表示する「データの中身」を決めるメソッド
    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get('sort')
        order = self.request.GET.get('order', 'asc')

        if sort == 'duedate':
            queryset = queryset.order_by('duedate' if order == 'asc' else '-duedate')
        elif sort == 'priority':
            # priority（文字列）を数値にマッピングして注釈し、その注釈でソートする
            queryset = queryset.annotate(
                priority_order=Case(
                    When(priority='danger', then=Value(1)),
                    When(priority='warning', then=Value(2)),
                    When(priority='primary', then=Value(3)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
            ).order_by('priority_order' if order == 'asc' else '-priority_order')

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_sort'] = self.request.GET.get('sort', '')
        context['current_order'] = self.request.GET.get('order', 'asc')
        return context

# DetailViewはリストの中から任意の一つを選んで詳細を表示する
# 何を表示するか明示する必要がある　URLにidを含める必要がある
class TodoDetail(DetailView):
    template_name = 'detail.html'
    model = TodoModel

class TodoCreate(CreateView):
    template_name = 'create.html'
    model = TodoModel
    # 作成成功後のリダイレクト先URL
    # reverse_lazy を使う理由は、クラス定義時にURLを遅延評価（＝必要になるまで解決しない）するため
    success_url = reverse_lazy('list') 
    form_class = TodoForm

class TodoDelete(DeleteView):
    template_name = 'delete.html'
    model = TodoModel
    success_url = reverse_lazy('list')

class TodoUpdate(UpdateView):
    template_name = 'update.html'
    model = TodoModel
    success_url = reverse_lazy('list')
    form_class = TodoForm

@require_POST
def todo_delete_direct(request, pk):
    todo = get_object_or_404(TodoModel, pk=pk)
    todo.delete()
    return redirect('list')