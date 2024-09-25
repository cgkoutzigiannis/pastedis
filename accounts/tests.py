from django.test import TestCase
from .models import CustomUser


class CustomUserModelTests(TestCase):
    def setUp(self):
        # Create a custom user.
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpassword123",
            first_name="Test",
            last_name="User",
        )

    def test_custom_user_creation(self):
        # Verify that the user was created successfully
        self.assertEqual(self.user.email, "testuser@example.com")
        self.assertTrue(self.user.check_password("testpassword123"))
        self.assertEqual(self.user.first_name, "Test")
        self.assertEqual(self.user.last_name, "User")
