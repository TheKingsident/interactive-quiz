from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('start_quiz', views.start_quiz, name="start-quiz"),
    path('add_quiz', views.add_quiz, name="add-quiz"),
]
