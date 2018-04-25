from django.test import TestCase

from django.contrib.auth.models import User
from apps.profile.models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Bob',
                email='bob@example.com', password='password')

    def test_auto_create_profile(self):
        "Check that a profile object is automatically created when adding a user"
        self.assertIsInstance(self.user.profile, Profile)
