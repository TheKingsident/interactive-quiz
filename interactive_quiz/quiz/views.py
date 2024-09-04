from django.shortcuts import render
from django.db import IntegrityError
import random
from .models import Quiz
from .forms import QuizForm, OptionFormSet
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'quiz/base.html')

def start_quiz(request):
    quiz_list = random.sample(list(Quiz.objects.all()), 3)
    
    return render(request, 'quiz/quiz.html', {
        "quiz_list": quiz_list
    })

def add_quiz(request):
    added = False
    if request.method == "POST":
        question_form = QuizForm(request.POST)
        option_formset = OptionFormSet(request.POST)

        if question_form.is_valid() and option_formset.is_valid():
            try:

                quiz = question_form.save()

                option_formset.instance = quiz
                option_formset.save()

                return HttpResponseRedirect('/add_quiz?added=True')
            except IntegrityError:
                question_form.add_error('question', 'This question already exists.')
    
    else:
        question_form = QuizForm()
        option_formset = OptionFormSet()

        if 'added' in request.GET:
            added = True

    for form in option_formset.forms:
        if 'DELETE' in form.fields:
            del form.fields['DELETE']

    return render(request, 'quiz/add_quiz.html', {
        'question_form': question_form,
        'option_formset': option_formset,
        'added': added
    })
