from django.db import models
from .word_level import WordLevel

class Word(models.Model):

    word = models.CharField(max_length=100)
    word_type = models.CharField(max_length=50)
    level = models.ForeignKey(WordLevel, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.word} ({self.level}, {self.word_type})"



