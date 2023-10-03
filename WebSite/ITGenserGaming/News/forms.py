from .models import Articls_News
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput

class Articles_News_Form(ModelForm):
    class Meta:
        model = Articls_News
        fields = ['title', 'anons', 'full_text', 'date']

        widgets ={
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название статьи'
            }),

            "anons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Анонс статьи'
            }),

            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст статьи'
            }),

            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата и время в формате: 01.01.2022 01:10:00'
            })
        }