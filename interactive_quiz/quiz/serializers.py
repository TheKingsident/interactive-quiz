from rest_framework import serializers
from .models import Quiz, Score, User, Option


class OptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Option
        fields = '__all__'

class QuizSerializer(serializers.ModelSerializer):
    options = OptionSerializer(many=True, read_only=True)
    class Meta:
        model = Quiz
        fields = ['id', 'question', 'answer', 'topic', 'difficulty', 'options']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    scores = ScoreSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'scores']
