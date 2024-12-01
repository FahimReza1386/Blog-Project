import pytest  # type: ignore
from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
from accounts.models import User
from blog.models import Category


@pytest.fixture
def api_client():
    client = APIClient()
    return client


@pytest.fixture
def common_user():
    user = User.objects.create_user(
        email="Fahimreza20200@gmail.com", password="Fahim2684"
    )
    return user


@pytest.fixture
def get_category():
    category = Category.objects.create(name="Test")
    return category


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200_status(self, api_client):
        url = reverse("blog:api-v1:post-list")
        response = api_client.get(url)
        assert response.status_code == 200

    def create_post_response_401_status(self, api_client, get_category):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "Hi-Test5-6",
            "content": "Test Content",
            "status": True,
            "category": get_category,
            "published_date": datetime.now(),
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_response_201_status(
        self, api_client, common_user, get_category
    ):
        url = reverse("blog:api-v1:post-list")
        data = {
            "title": "Hi-Test5-6",
            "content": "Test Content",
            "status": True,
            "category": get_category,
            "published_date": datetime.now(),
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201, response.content

    def test_create_post_invalid_data_response_400_status(
        self, api_client, common_user
    ):
        url = reverse("blog:api-v1:post-list")
        data = {"title": "Hi-Test5-6", "content": "Test Content", "status": True}
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400, response.content
