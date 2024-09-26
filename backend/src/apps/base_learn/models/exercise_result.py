from django.db import models
from django.contrib.auth.models import User
from .exercise import Exercise
from .words import Word

class ExerciseResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    success = models.BooleanField()

    def __str__(self):
        return f"{self.user.username} - {self.exercise.type} - {self.word.word}: {'Success' if self.success else 'Failure'}"
