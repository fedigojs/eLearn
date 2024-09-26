import pandas as pd
from django.core.management.base import BaseCommand
from base_learn.models import Word, WordLevel

class Command(BaseCommand):
    help = 'Import words from an XLSX file into the Word model'

    def add_arguments(self, parser):

        parser.add_argument('xlsx_file', type=str, help='The path to the XLSX file containing words')

    def handle(self, *args, **kwargs):
        xlsx_file = kwargs['xlsx_file']

        df = pd.read_excel(xlsx_file)

        for index, row in df.iterrows():
            word_full = row[0]
            level = row[1]

            parts = word_full.split(' ')
            word = parts[0]
            word_type = ' '.join(parts[1:])

            word_level = WordLevel.objects.get(level=level)

            Word.objects.get_or_create(
                word=word,
                word_type=word_type,
                level=word_level,
            )

        self.stdout.write(self.style.SUCCESS('Successfully imported words from XLSX file'))
