from django.core.management.base import BaseCommand, CommandError
from faker import Faker  # type: ignore
from accounts.models import Profile, User
from blog.models import Post, Category


class Command(BaseCommand):
    help = "inserting dummy data."

    def __init__(self, *args , **kwargs):
        super().__init__(*args , **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(email = self.fake.email() , password=self.fake.password())
        user.is_verified = True
        user.save()
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=3)
        profile.save()
        print(profile)