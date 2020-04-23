from django.test import TestCase
from django.contrib.auth.models import User
from accounts.forms import UserRegistrationForm, UserLoginForm

class AccountsFormsTests(TestCase):

    def test_valid_user_registration_form(self):
        form = UserRegistrationForm({
            'username': 'mike-d',
            'email': 'mikedhiggins@test.com',
            'password1': 'wizard1',
            'password2': 'wizard1'
        })

        self.assertTrue(form.is_valid())
    
    
    def test_login_template(self):
        response = self.client.get("/accounts/login", follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('login.html')