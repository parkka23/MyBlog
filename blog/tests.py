from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import PostModel


class UserAuthenticationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123'
        }
        self.post_data = {
            'title': 'Test Post',
            'content': 'This is a test post content.'
        }

    def test_signup(self):
        response = self.client.post(self.signup_url, self.user_data)
        self.assertEqual(response.status_code, 302)  # Redirects after successful signup
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_login(self):
        User.objects.create_user(username='testuser', password='testpassword123')
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'testpassword123'})
        self.assertEqual(response.status_code, 302)  # Redirects after successful login
        self.assertTrue('_auth_user_id' in self.client.session)

    def test_create_post(self):
        user = User.objects.create_user(username='testuser', password='testpassword123')
        self.client.login(username='testuser', password='testpassword123')
        create_post_url = reverse('create-post')
        response = self.client.post(create_post_url, self.post_data)
        self.assertEqual(response.status_code, 302)  # Redirects after creating a post
        self.assertTrue(PostModel.objects.filter(title='Test Post', author=user).exists())
