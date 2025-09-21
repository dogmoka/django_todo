from django import forms
from .models import TodoModel

class TodoForm(forms.ModelForm):
    class Meta:
        model = TodoModel
        fields = ['title', 'memo', 'priority', 'duedate']
        widgets = {
            'duedate': forms.DateInput(attrs={'type': 'date'}),
        }