from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Score(models.Model):
    score = models.IntegerField()
    user = models.ForeignKey(User, related_name='scores', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.score}"

class Quiz(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    topic = models.CharField(max_length=200, blank=True)
    difficulty = models.CharField(max_length=200)
    added_by = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.question
    
class Option(models.Model):
    option_text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, related_name='options', on_delete=models.CASCADE)

    def __str__(self):
        return self.option_text
