# from django.test import TestCase
# from django.urls import reverse
# # Create your tests here.
#
# class BaseTest(TestCase):
#     def setUp(self):
#         self.register_url=reverse('sign_up')
#         # self.user={
#         #     'email':'test@gmail.com',
#         #     'username':'username',
#         #     'password':'password',
#         #     ''
#         #
#         # }
#         return super().setUp()
#
# class RegisterTest(BaseTest):
#     def test_can_view_page_correctly(self):
#         response=self.client.get(self.register_url)
#         self.assertEqial(response.status_code,200)
#         self.assertTemplateUser(response,'user/sign_up.html')

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class UserSignUpTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('users-sign-up')
        self.user_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
        }

    def test_signup(self):
        response = self.client.post(self.signup_url, self.user_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.filter(username='testuser').exists())


class UserLoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('users-login')
        self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='TestPassword123!')

    def test_login(self):
        response = self.client.post(self.login_url, {'username': 'testuser', 'password': 'TestPassword123!'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('_auth_user_id' in self.client.session)
