import csv
from django.core.management.base import BaseCommand
from catalog.models import Phone

class Command(BaseCommand):
    help = 'Import phones from CSV file'

    def handle(self, *args, **options):
        file_path = 'phones.csv'

        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                phone = Phone(
                    id=int(row['id']),
                    name=row['name'],
                    price=float(row['price']),
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'].lower() == 'true',
                    slug=None
                )
                phone.save()
                self.stdout.write(f'Добавлен: {phone.name}')

        self.stdout.write(self.style.SUCCESS('Импорт завершён!'))