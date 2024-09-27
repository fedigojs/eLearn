from ninja import Router
from .schema import ExerciseRequest
from apps.base_learn.models import Word
from django.shortcuts import get_object_or_404

router = Router()

@router.post("/exercise/check_translation")
def check_translation(request, data: ExerciseRequest):
    word = get_object_or_404(Word, id=data.word_id)
    is_correct = (word.translation == data.answer)
    return {"correct": is_correct}
