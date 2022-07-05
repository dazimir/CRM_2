from .models import Task
from .models import Authentication
from django.forms import ModelForm, TextInput, Textarea, DateInput, SelectDateWidget, SplitDateTimeField


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'task']
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'название задачи 2'}),
            "tasks": Textarea(attrs={'class': 'form-control', 'placeholder': 'текст задачи 2'})
        }


class AuthenticationForm(ModelForm):
    class Meta:
        model = Authentication
        fields = {'user_nickname', 'user_name', 'user_lastname', 'user_patronymic', 'user_birthday',
                  'user_registration', 'user_phone', 'user_email', 'user_photo', 'user_rang'}
        widgets = {
            "user_nickname": TextInput(attrs={'class': 'form-control', 'placeholder': 'Никнейм'}),
            "user_name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Имя оператора'}),
            "user_lastname": TextInput(attrs={'class': 'form-control', 'placeholder': 'Фамилия оператора'}),
            "user_patronymic": TextInput(attrs={'class': 'form-control', 'placeholder': 'Отчество оператора'}),
            "user_birthday": DateInput(),
            "user_registration": DateInput(),
            "user_phone": TextInput(attrs={'class': 'form-control', 'placeholder': 'Телефон оператора'}),
            "user_email": TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            "user_photo": TextInput(attrs={'class': 'form-control', 'placeholder': 'Фото'}),
            "user_rang": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ранг'})
        }
        print(widgets)