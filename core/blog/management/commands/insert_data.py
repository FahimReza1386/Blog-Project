from django.core.management.base import BaseCommand
from faker import Faker  # type: ignore
from accounts.models import Profile, User
from blog.models import Post, Category
from datetime import datetime
import random

category_name = ["IT", "Fun", "Programming", "Trading"]


class Command(BaseCommand):

    help = "inserting dummy data."

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            email=self.fake.email(), password=self.fake.password()
        )
        user.is_verified = True
        user.save()
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=3)
        profile.save()
        print(profile)

        for name in category_name:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Post.objects.create(
                author=profile,
                title=self.fake.paragraph(nb_sentences=1),
                content=self.fake.paragraph(nb_sentences=5),
                status=random.choice([True, False]),
                category=Category.objects.get(name=random.choice(category_name)),
                published_date=datetime.now(),
            )
