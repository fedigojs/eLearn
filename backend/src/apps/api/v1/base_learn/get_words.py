from ninja import Router

router = Router()

@router.get("/words")
def get_words(request):
    return {"word": "example", "meaning": "An instance of something"}
