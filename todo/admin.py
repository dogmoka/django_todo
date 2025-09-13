from django.contrib import admin

from todo.models import TodoModel

# Register your models here.

# 管理者画面のDBにmodelsに加えたものを反映させる
admin.site.register(TodoModel)