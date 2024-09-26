from django.contrib.auth.models import User
from django.db import models
from .words import Word

class UserWordProgress(models.Model):
    STATUS_CHOICES = [
        ('to_learn', 'Need to learn'),
        ('learning', 'Learning'),
        ('learned', 'Learned'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    word = models.ForeignKey(Word, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='to_learn')

    class Meta:
        unique_together = ('user', 'word')

    def __str__(self):
        return f"{self.user.username} - {self.word.word}: {self.status}"
