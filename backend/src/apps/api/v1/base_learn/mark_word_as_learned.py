from ninja import Router
from django.contrib.auth.models import User
from apps.base_learn.models import UserWordProgress
from django.shortcuts import get_object_or_404

router = Router()

@router.post("/word/{word_id}/learned")
def mark_word_as_learned(request, word_id: int, user_id: int):
    user = get_object_or_404(User, id=user_id)
    progress = get_object_or_404(UserWordProgress, word_id=word_id, user=user)
    progress.status = 'learned'
    progress.save()
    return {"status": "success"}
