from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm, inlineformset_factory
from .models import Quiz, Option


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ('question', 'answer', 'topic', 'difficulty')
        labels = {
            'question': '',
            'name': '',
            'answer': '',
            'topic': '',
            'difficulty': ''
        }

        widgets = {
            'question': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Question'}),
            'answer': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Answer'}),
            'topic': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Topic'}),
            'difficulty': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Difficulty'}) 
        }

    def clean_question(self):
        question = self.cleaned_data.get('question')
        if Quiz.objects.filter(question=question).exists():
            raise ValidationError("This question has already been added.")
        return question

OptionFormSet = inlineformset_factory(Quiz, Option, fields=('option_text',), extra=4)
