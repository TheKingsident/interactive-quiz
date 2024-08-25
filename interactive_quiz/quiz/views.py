from django.shortcuts import render
from datetime import datetime
from .models import Quiz

# Create your views here.
def home(request):
    return render(request, 'quiz/base.html')

def start_quiz(request):
    quiz_list = Quiz.objects.all()
    return render(request, 'quiz/quiz.html', {
        "quiz_list": quiz_list
    })
