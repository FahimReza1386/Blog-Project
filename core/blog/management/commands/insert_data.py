from django.core.management.base import BaseCommand, CommandError
from faker import Faker  # type: ignore

class Command(BaseCommand):
    help = "inserting dummy data."

    def handle(self, *args, **options):
        fake=Faker()
        print(fake.name())
        print(fake.job())
