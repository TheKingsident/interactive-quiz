from rest_framework import viewsets
from .models import Quiz, User
from .serializers import QuizSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny


class QuizViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    permission_classes = [AllowAny]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
