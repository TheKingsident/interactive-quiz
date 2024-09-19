from django.shortcuts import render, redirect
from django.db import IntegrityError
import random
from .models import Quiz, Score, Option
from .forms import QuizForm, OptionFormSet
from django.http import HttpResponseRedirect
from django.contrib import messages

def home(request):
    return render(request, 'quiz/base.html')

def start_quiz(request, topic):
    if topic == "all":
        quiz_list = random.sample(list(Quiz.objects.all()), 10)
    elif topic == "others":
        quiz_list = Quiz.objects.filter(topic__isnull=True) | Quiz.objects.filter(topic='')
    else:
        quiz_list = Quiz.objects.filter(topic=topic)


    if request.method == "POST":
        quiz_list = request.session.get('quiz_list', [])

        score = 0

        for quiz_id in quiz_list:
            try:
                quiz = Quiz.objects.get(id=quiz_id)
                selected_option_id = request.POST.get(f"option_{quiz.id}")

                if selected_option_id:
                
                    selected_option = Option.objects.get(id=selected_option_id)

                    if selected_option.option_text == quiz.answer:
                        score += 1
            except Quiz.DoesNotExist:
                pass
            except Option.DoesNotExist:
                    pass

        score_obj = Score.objects.create(user = request.user, score=score)
        score_obj.save()

        messages.success(request, f'You scored {score} out of {len(quiz_list)}!')
        return redirect('home')
    
    else:
        quiz_list = random.sample(list(quiz_list), min(10, len(quiz_list)))
        request.session['quiz_list'] = [quiz.id for quiz in quiz_list]

    return render(request, 'quiz/quiz.html', {
        "quiz_list": quiz_list,
        "topic": topic,
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

def quiz_topics(request):
    topics_list = Quiz.objects.values_list('topic', flat=True).distinct().order_by('topic')
    return render(request, 'quiz/topics.html', {
        'topics_list': topics_list
    })
