
from django.contrib import admin
from django.urls import include, path
from .views import TodoList, TodoDetail, TodoCreate, TodoDelete, TodoUpdate, todo_delete_direct

urlpatterns = [
    # URLにname属性をつけておくと、テンプレートやViewで参照しやすくなる
    path('list/', TodoList.as_view(), name='list'),
    path('detail/<int:pk>', TodoDetail.as_view(), name='detail'), 
    path('create/', TodoCreate.as_view(), name='create'),
    path('delete/<int:pk>', TodoDelete.as_view(), name='delete'),
    path('update/<int:pk>', TodoUpdate.as_view(), name='update'),
    path('delete_direct/<int:pk>/', todo_delete_direct, name='delete_direct'),
]
