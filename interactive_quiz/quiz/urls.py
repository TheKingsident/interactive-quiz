from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import QuizViewSet, UserViewSet
from . import views

router = DefaultRouter()
router.register(r'quizzes', QuizViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', views.home, name="home"),
    path('start_quiz', views.start_quiz, name="start-quiz"),
    path('add_quiz', views.add_quiz, name="add-quiz"),
    path('api/', include(router.urls)),
]
