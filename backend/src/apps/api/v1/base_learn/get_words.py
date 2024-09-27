from ninja import Router
from apps.base_learn.models import Word

router = Router()

@router.get("/words")
def get_words(request):
    words = Word.objects.all()
    return [{"word": word.word, "level": word.level.level, "type": word.word_type} for word in words]
