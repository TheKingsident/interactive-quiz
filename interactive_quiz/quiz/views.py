from django.shortcuts import render
import random
from datetime import datetime
from .models import Quiz
from .forms import QuizForm

# Create your views here.
def home(request):
    return render(request, 'quiz/base.html')

def start_quiz(request):
    quiz_list = random.sample(list(Quiz.objects.all()), 3)
    
    return render(request, 'quiz/quiz.html', {
        "quiz_list": quiz_list
    })

def add_quiz(request):
    return render(request, 'quiz/add_quiz.html')
