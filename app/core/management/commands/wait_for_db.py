import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Waiting for database...')
        db_up = False
        attempts = 0  # Counter for debugging
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError) as e:
                attempts += 1  # Increment attempts counter
                self.stdout.write(self.style.WARNING('Database is available'))
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available'))

    def check(self, *args, **kwargs):
        # Mock implementation for testing
        pass
