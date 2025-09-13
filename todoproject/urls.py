
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # appのurls.pyを参照するように設定
    # admin以外のパスはすべてtodoアプリに任せる
    path('', include('todo.urls')),
]
