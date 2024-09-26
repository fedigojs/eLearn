from django.db import models
from django.contrib.auth.models import User
from .exercise import Exercise

class UserExerciseRating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(default=0)

    class Meta:
        unique_together = ('user', 'exercise')

    def __str__(self):
        return f"{self.user.username} - {self.exercise.type}: {self.rating}"
