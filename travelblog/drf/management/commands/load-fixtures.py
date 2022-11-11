from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")
        call_command("loaddata", "db_homepage_fixture.json")
        User.objects.create_superuser('test@example.com', 'test','test')
