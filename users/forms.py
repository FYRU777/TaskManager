from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'start_date', 'end_date']
        labels = {
            'title': 'Название Задачи:',
            'description': 'Описание:',
            'start_date': 'Начало:',
            'end_date': 'Конец',
        }

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
