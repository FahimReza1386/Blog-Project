from django.test import TestCase
from ..models import Post
from datetime import datetime
from accounts.models import User, Profile


class TestPostModel(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(email='Ali987@gmail.com', password="ali/@12345")
        self.profile = Profile.objects.create(user=self.user)

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            title='Hi-Test5-6',
            content='Test Content',
            status=True,
            category=None,
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
