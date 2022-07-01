from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'название задачи 2'}),
            "tasks": Textarea(attrs={'class': 'form-control', 'placeholder': 'текст задачи 2'})
        }
#  из дома
