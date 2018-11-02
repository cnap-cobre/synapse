from allauth.socialaccount.providers import registry
from apps.profile.models import Profile
from apps.profile import util
from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase
from rest_framework.test import APIClient
from .api.views import ProfileViewSet


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='Bob',
            email='bob@example.com',
            password='password'
        )

    def test_auto_create_profile(self):
        # Check that a profile object is automatically
        # created when adding a user
        self.assertIsInstance(self.user.profile, Profile)

    def test_oauth_refresh_token_url_resolution(self):
        for provider in registry.get_list():
            self.assertTrue(
                'https' in util.get_provider(provider.id).profile_url
            )

    def test_oauth_get_protected_url(self):
        for provider in registry.get_list():
            self.assertTrue(
                'https' in util.get_provider(provider.id).access_token_url
            )


class ProfileAPIPermissionsTestCase(TestCase):
    def setUp(self):
        # 1. Create a regular user
        # 2. Create a super user
        # 3. Create a regular user with the
        #    profile.can_view_full_profiles_of_others permission
        # 4. Create a group with can_view_full_profiles_of_others
        #    permission and a user in that group
        view_permission = Permission.objects.get(
            codename='can_view_full_profiles_of_others'
        )

        # 1.
        self.regular_user = User.objects.create_user(
            username='morty',
            email='morty@rickandmorty.com',
            password='gazorpazorp'
        )

        # 2.
        self.super_user = User.objects.create_superuser(
            username='meeseeks',
            email='meseeks@rickandmorty.com',
            password='caaaaaaaannnndoooooo'
        )

        # 3.
        self.regular_user_with_perm = User.objects.create_user(
            username='rick',
            email='rick@rickandmorty.com',
            password='wubalubadubdub'
        )
        self.regular_user_with_perm.user_permissions.add(view_permission)

        # 4.
        approved_group = Group.objects.create(name='Approved Users')
        approved_group.permissions.add(view_permission)
        self.regular_user_in_group = User.objects.create_user(
            username='jerry',
            email='jerry@rickandmorty.com',
            password='asdfasdf'
        )
        self.regular_user_in_group.groups.add(approved_group)

    def test_profiles_were_auto_created(self):
        self.assertIsInstance(self.regular_user.profile, Profile)
        self.assertIsInstance(self.super_user.profile, Profile)
        self.assertIsInstance(self.regular_user_with_perm.profile, Profile)

        self.assertTrue(self.super_user.is_staff)
        self.assertTrue(self.super_user.is_superuser)

    def test_permission_resolved_as_expected(self):
        self.assertFalse(
            self.regular_user.has_perm(
                'profile.can_view_full_profiles_of_others'
            )
        )
        self.assertTrue(
            self.super_user.has_perm(
                'profile.can_view_full_profiles_of_others'
            )
        )
        self.assertTrue(
            self.regular_user_with_perm.has_perm(
                'profile.can_view_full_profiles_of_others'
            )
        )
        self.assertTrue(
            self.regular_user_in_group.has_perm(
                'profile.can_view_full_profiles_of_others'
            )
        )

    def test_anon_should_be_forbidden(self):
        client = APIClient()
        some_uid = self.regular_user.id

        # API Root
        self.assertEqual(
            client.get('/api/v1/', format='json').status_code,
            403
        )

        # List
        self.assertEqual(
            client.get('/api/v1/profiles/', format='json').status_code,
            403
        )
        self.assertEqual(
            client.head('/api/v1/profiles/', format='json').status_code,
            403
        )
        self.assertEqual(
            client.options('/api/v1/profiles/', format='json').status_code,
            403
        )

        # Create New
        self.assertEqual(client.post('/api/v1/profiles/', {
            'institution': 'Kansas State University'
        }, format='json').status_code, 403)

        # Individual
        self.assertEqual(
            client.get(
                '/api/v1/profiles/%d/' % some_uid,
                format='json'
            ).status_code,
            403
        )
        self.assertEqual(client.put('/api/v1/profiles/%d/' % some_uid, {
            'institution': 'Kansas State University'
        }, format='json').status_code, 403)
        self.assertEqual(client.patch('/api/v1/profiles/%d/' % some_uid, {
            'institution': 'Kansas State University'
        }, format='json').status_code, 403)
        self.assertEqual(
            client.delete(
                '/api/v1/profiles/%d/' % some_uid,
                format='json'
            ).status_code,
            403
        )
        self.assertEqual(
            client.head(
                '/api/v1/profiles/%d/' % some_uid,
                format='json'
            ).status_code,
            403
        )
        self.assertEqual(
            client.options(
                '/api/v1/profiles/%d/' % some_uid,
                format='json'
            ).status_code,
            403
        )

    def test_anon_can_create_new_user_which_can_not_delete_itself(self):
        client = APIClient()

        self.assertEqual(client.options('/api/v1/users/').status_code, 200)

        # Create it
        self.assertEqual(client.post('/api/v1/users/', {
            'first_name': 'Ron',
            'last_name': 'Weasley',
            'username': 'ron',
            'email': 'ron@harrypotter.com',
            'password': 'follow the spiders?!?!'
        }, format='json').status_code, 201)

        # Delete it
        ron_id = User.objects.filter(username='ron').get().id
        self.assertEqual(
            client.delete('/api/v1/users/%d/' % ron_id).status_code,
            403
        )

    def test_anon_can_not_create_new_staff_user(self):
        client = APIClient()

        self.assertEqual(client.post('/api/v1/users/', {
            'first_name': 'Peter',
            'last_name': 'Pan',
            'username': 'pete',
            'email': 'pete@neverland.com',
            'is_staff': True
        }, format='json').status_code, 400)

    def test_regular_user_should_have_limited_view_of_profile_list(self):
        client = APIClient()
        client.force_authenticate(user=self.regular_user)

        # API Root
        self.assertEqual(
            client.get('/api/v1/', format='json').status_code,
            200
        )

        # List
        list_response = client.get('/api/v1/profiles/', format='json')
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(
            set(list_response.data[0]['user'].keys()),
            set(['id', 'username', 'url']))
        self.assertEqual(
            client.head('/api/v1/profiles/', format='json').status_code,
            200
        )
        self.assertEqual(
            client.options('/api/v1/profiles/', format='json').status_code,
            200
        )

    def test_regular_user_can_view_own_profile_in_full(self):
        client = APIClient()
        client.force_authenticate(user=self.regular_user)
        id = self.regular_user.id

        single_response = client.get(
            '/api/v1/profiles/%d/' % id,
            format='json'
        )
        self.assertEqual(single_response.status_code, 200)
        self.assertTrue(
            set(['first_name', 'last_name', 'email', 'groups']).issubset(
                set(single_response.data['user'].keys())
            )
        )

    def test_regular_user_can_create_new_users(self):
        client = APIClient()
        client.force_authenticate(user=self.regular_user)

        # Create New - Should fail with disallowed field
        self.assertEqual(client.post('/api/v1/users/', {
            'first_name': 'Peter',
            'last_name': 'Pan',
            'username': 'pete',
            'email': 'pete@neverland.com',
            'is_staff': True,
            'password': 'neverneverland'
        }, format='json').status_code, 400)

        # Create New - Should succeed
        self.assertEqual(client.post('/api/v1/users/', {
            'first_name': 'Peter',
            'last_name': 'Pan',
            'username': 'pete',
            'email': 'pete@neverland.com',
            'password': 'neverneverland'
        }, format='json').status_code, 201)

        # Create New - Should fail as duplicate username
        self.assertEqual(client.post('/api/v1/users/', {
            'first_name': 'Peter',
            'last_name': 'Pan',
            'username': 'pete',
            'email': 'pete@neverland.com',
            'password': 'neverneverland'
        }, format='json').status_code, 400)

    def test_regular_user_can_not_update_profiles_of_others(self):
        client = APIClient()
        client.force_authenticate(user=self.regular_user)

        # Update Existing Profile - Should fail due to lack of ownership
        other_id = self.regular_user_with_perm.id
        self.assertEqual(client.patch('/api/v1/profiles/%d/' % other_id, {
            'institution': 'University of Kansas'
        }, format='json').status_code, 403)

    def test_regular_user_can_update_own_profile(self):
        client = APIClient()
        client.force_authenticate(user=self.regular_user)

        # Partially Update Existing Profile
        #  - Should succeed because of ownership
        self.assertEqual(
            client.patch(
                '/api/v1/profiles/%d/' % self.regular_user.id,
                {'institution': 'Washington State University'},
                format='json'
            ).status_code,
            200
        )
        self.assertEqual(
            Profile.objects.filter(
                user_id=self.regular_user.id
            ).get().institution,
            'Washington State University'
        )

        # Full update of existing profile
        #  - should succeed because of ownership
        self.assertEqual(
            client.put(
                '/api/v1/profiles/%d/' % self.regular_user.id,
                {'institution': 'Wichita State University'},
                format='json'
            ).status_code,
            200
        )
        self.assertEqual(
            Profile.objects.filter(
                user_id=self.regular_user.id
            ).get().institution,
            'Wichita State University'
        )

    def test_privileged_user_can_see_full_profiles(self):
        client = APIClient()
        client.force_authenticate(user=self.regular_user_with_perm)

        user_list_response = client.get('/api/v1/users/', format='json')
        self.assertEqual(user_list_response.status_code, 200)
        self.assertTrue('groups' in user_list_response.data[0].keys())
        self.assertTrue('email' in user_list_response.data[0].keys())

        profile_list_response = client.get('/api/v1/profiles/', format='json')
        self.assertEqual(profile_list_response.status_code, 200)
        self.assertTrue(
            'groups' in profile_list_response.data[0]['user'].keys()
        )
        self.assertTrue(
            'email' in profile_list_response.data[0]['user'].keys()
        )

    def test_user_profile_me_endpoint(self):
        client = APIClient()
        client.force_authenticate(user=self.regular_user)

        my_user = client.get('/api/v1/users/me/', format='json')
        self.assertEqual(my_user.status_code, 200)
        self.assertDictContainsSubset({
            'username': 'morty',
            'email': 'morty@rickandmorty.com'
        }, my_user.data)

        my_profile = client.get('/api/v1/profiles/me/', format='json')
        self.assertEqual(my_profile.status_code, 200)
        self.assertDictContainsSubset({
            'username': 'morty',
            'email': 'morty@rickandmorty.com'
        }, my_profile.data['user'])
