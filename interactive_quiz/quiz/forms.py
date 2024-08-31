from django import forms
from django.forms import ModelForm
from .models import Quiz, Option


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ('question', 'answer', 'topic', 'difficulty', 'added_by')
        