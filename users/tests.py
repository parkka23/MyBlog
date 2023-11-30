from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class BaseTest(TestCase):
    def setUp(self):
        self.register_url=reverse('sign_up')
        # self.user={
        #     'email':'test@gmail.com',
        #     'username':'username',
        #     'password':'password',
        #     ''
        #
        # }
        return super().setUp()

class RegisterTest(BaseTest):
    def test_can_view_page_correctly(self):
        response=self.client.get(self.register_url)
        self.assertEqial(response.status_code,200)
        self.assertTemplateUser(response,'user/sign_up.html')
