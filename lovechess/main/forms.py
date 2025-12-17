from django.forms import ModelForm, TextInput, Textarea
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        widgets = {
            "title": TextInput(attrs={
                'class':'form-control',
                'placeholder':'Введите название'
            }),
             "description": Textarea(attrs={
                'class':'form-control',
                'placeholder':'Введите описание'
            }),
        }