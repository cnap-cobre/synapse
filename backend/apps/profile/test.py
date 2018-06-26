from allauth.socialaccount.providers import registry
from apps.profile.models import Profile
from apps.profile import util
from django.contrib.auth.models import User
from django.test import TestCase


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Bob',
                email='bob@example.com', password='password')

    def test_auto_create_profile(self):
        "Check that a profile object is automatically created when adding a user"
        self.assertIsInstance(self.user.profile, Profile)

    def test_oauth_refresh_token_url_resolution(self):
        for provider in registry.get_list():
            self.assertTrue('https' in
                    util.get_provider(provider.id).profile_url)

    def test_oauth_get_protected_url(self):
        for provider in registry.get_list():
            self.assertTrue('https' in
                    util.get_provider(provider.id).access_token_url)