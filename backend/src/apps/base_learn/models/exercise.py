from django.db import models


class Exercise(models.Model):
    EXERCISE_TYPES = [
        ('translate_native', 'Перевод с родного языка'),
        ('choose_translation', 'Выбор правильного перевода'),
        ('fill_in_blanks', 'Заполнение пропусков'),
        ('match_image', 'Сопоставление слова и изображения'),
        ('audio_test', 'Аудио-тест'),
        ('spell_word', 'Правописание слова'),
        ('define_word', 'Определение слова'),
        ('sort_by_meaning', 'Сортировка по значению'),
        ('word_cascade', 'Словесный каскад'),
        ('flashcards', 'Карточки'),
        ('crossword', 'Кроссворд'),
        ('find_word', 'Найди слово'),
    ]

    type = models.CharField(max_length=50, choices=EXERCISE_TYPES)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.get_type_display()
