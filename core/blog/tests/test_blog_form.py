from django.test import TestCase
from ..forms import PostForm
from datetime import datetime
from ..models import Category


class TestPostForm(TestCase):
    def test_post_form_with_valid_data(self):
        category = Category.objects.create(name="hi")
        form = PostForm(
            data={
                "title": "Ali",
                "content": "Hi Ali",
                "status": "True",
                "category": category.id,
                "published_date": datetime.now(),
            }
        )

        self.assertTrue(form.is_valid())

    def test_blog_form_with_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())