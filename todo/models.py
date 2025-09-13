from django.db import models

# Create your views here.


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # DB上での表示名
    def __str__(self):
        return self.title
