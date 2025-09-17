from django.db import models

# Create your views here.


class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=10,
        choices=(
            # (DB上の値, 管理画面などで表示される値)
            # DB上の値はlist.htmlのclass名に使われる
            ('primary', '低'),
            ('warning', '中'),
            ('danger', '高'),
        ),
        default='warning',
    )
    duedate = models.DateField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # DB上での表示名
    def __str__(self):
        return self.title
