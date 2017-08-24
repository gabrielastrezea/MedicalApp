
from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):

    help = "Load intial data"

    def handle(self, *args, **options):
        for fixture in ('users', 'doctors', 'patients', 'medicine'):
            call_command('loaddata', fixture)
