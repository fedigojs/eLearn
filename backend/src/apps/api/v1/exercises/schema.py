from ninja import Schema

class ExerciseRequest(Schema):
    word_id: int
    answer: str