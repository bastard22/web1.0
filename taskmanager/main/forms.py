from django.forms import ModelForm, TextInput, Textarea
from django import forms
from .models import *

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["title", "task"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'WRITE TASK'
            }),
            "task": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'WRITE WHAT'
            })
        }

class nenad(forms.ModelForm):
    class Meta:
        model = nenad
        fields = ['name', 'nenad_main_img']