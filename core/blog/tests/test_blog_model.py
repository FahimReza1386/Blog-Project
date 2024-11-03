from django.test import SimpleTestCase , TestCase
from ..models import *
from datetime import datetime
from django.contrib.auth import  get_user_model
from accounts.models import User , Profile
class TestPostModel(TestCase):
    def test_create_post_with_valid_data(self):
        user=User.objects.create_user(email='Ali987@gmail.com' , password="ali/@12345")
        profile=Profile.objects.create(user=user)
        post = Post.objects.create(
            author=profile,
            title='Hi-Test5-6' , 
            content='Test Content' ,
            status=True , 
            category=None, 
            published_date=datetime.now() ,
        )
        self.assertEquals(post.title , 'Hi-Test5-6')