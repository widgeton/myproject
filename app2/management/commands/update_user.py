from django.core.management.base import BaseCommand
from app2.models import User


class Command(BaseCommand):
    help = "Update user name by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')
        parser.add_argument('name', type=str, help='User name')

    def handle(self, *args, **options):
        pk = options.get('pk')
        name = options.get('name')
        user = User.objects.filter(pk=pk).first()
        if user is not None:
            user.name = name
            user.save()
        self.stdout.write(f'{user}')
