from ninja import Router
from django.contrib.auth.models import User
from apps.base_learn.models import UserWordProgress
from django.shortcuts import get_object_or_404

router = Router()

@router.get("/words/to_learn/{user_id}")
def get_words_to_learn(request, user_id: int):
    user = get_object_or_404(User, id=user_id)
    words = UserWordProgress.objects.filter(user=user, status='to_learn').select_related('word')
    return [{"word": progress.word.word, "translation": progress.word.translation, "level": progress.word.level.level} for progress in words]
