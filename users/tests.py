from django.contrib.auth.models import User
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase


class UserRegistrationAPITestCase(APITestCase):
    def setUp(self):
        self.fake = Faker()

    def test_user_registration(self):
        url = reverse("user-registration")
        data = {
            "username": self.fake.user_name(),
            "email": self.fake.email(),
            "password": self.fake.password(),
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, data["username"])

    def test_user_login(self):
        user = User.objects.create_user(username="testuser", password="testpassword")
        url = reverse("user-login")
        data = {"username": user.username, "password": "testpassword"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("token", response.data)
        self.assertIn("id", response.data)
