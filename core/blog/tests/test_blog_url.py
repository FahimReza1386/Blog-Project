from django.test import TestCase
from django.urls import reverse, resolve
from ..views import indexview, Posts, PostDetails

# Create your tests here.


class TestUrl(TestCase):
    def test_blog_index_url_resolve(self):
        url = reverse("blog:index")
        self.assertEquals(resolve(url).func.view_class, indexview)

    def test_blog_post_list_url_resolve(self):
        url = reverse("blog:post-listApi")
        self.assertEqual(resolve(url).func.view_class, Posts)

    def test_blog_post_detail_url_resolve(self):
        url = reverse("blog:post-detail", kwargs={"pk": 1})
        self.assertEqual(resolve(url).func.view_class, PostDetails)
