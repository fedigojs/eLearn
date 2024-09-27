from ninja import Router
from apps.base_learn.models import Word

router = Router()

@router.get("/word/{word_id}")
def get_word_by_id(request, word_id: int):
    word = Word.objects.get(id=word_id)
    return {
        "word": word.word,
        "level": word.level.level,
        "type": word.word_type
    }