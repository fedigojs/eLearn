from django.db import models

class WordLevel(models.Model):
    level = models.CharField(max_length=2, choices=[
        ('A1', 'Beginner (A1)'),
        ('A2', 'Elementary (A2)'),
        ('B1', 'Intermediate (B1)'),
        ('B2', 'Upper-Intermediate (B2)'),
        ('C1', 'Advanced (C1)'),
        ('C2', 'Proficient (C2)'),
    ])
    description = models.TextField()

    def __str__(self):
        return self.level

