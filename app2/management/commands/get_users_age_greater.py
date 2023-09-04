from django.core.management.base import BaseCommand
from app2.models import User


class Command(BaseCommand):
    help = "Get user with age greater <age>."

    def add_arguments(self, parser):
        parser.add_argument('age', type=int, help='User age')

    def handle(self, *args, **options):
        age = options['age']
        users = User.objects.filter(age__gt=age)
        self.stdout.write(f'{users}')
