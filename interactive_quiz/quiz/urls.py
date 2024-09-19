from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import QuizViewSet, UserViewSet
from . import views

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('start_quiz/<str:topic>', views.start_quiz, name="start-quiz"),
    path('add_quiz', views.add_quiz, name="add-quiz"),
    path('topics', views.quiz_topics, name="topics"),

    path('api/', include(router.urls)),
]
