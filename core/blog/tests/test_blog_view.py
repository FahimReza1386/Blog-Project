from django.test import TestCase,Client
from django.urls import resolve , reverse
from accounts.models import User , Profile
from blog.models import Category , Post
from datetime import datetime
class TestBlogView(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='Ali987@gmail.com' , password="ali/@12345")
        self.profile = Profile.objects.create(user=self.user)
        self.post = Post.objects.create(
            author=self.profile,
            title='Hi-Test5-6' , 
            content='Test Content' ,
            status=True , 
            image='111',
            category=None, 
            published_date=datetime.now() ,
        )



    def test_blog_index_response_200(self):
        url = reverse("blog:index")
        response = self.client.get(url)
        self.assertEquals(response.status_code , 200)
        self.assertTrue(str(response.content).find('index'))
        self.assertTemplateUsed(response ,template_name="base.html")


    def test_blog_post_detail_logged_in_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail' , kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code , 200)



    def test_blog_post_detail_anonymous_response(self):
        url = reverse("blog:post-detail" , kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEquals(response.status_code , 302)