from django.contrib.auth import get_user_model
from django.test import TestCase
from .forms import RegistrationForm

class UsersManagersTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='normal@user.com', password='foo',username='foo',last_name='bar',first_name='bear')
        self.assertEqual(user.email, 'normal@user.com')
        self.assertEqual(user.last_name, 'bar')
        self.assertEqual(user.first_name, 'bear')
        self.assertFalse(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superadmin)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='supr@user.com', password='foo',username='el',last_name='bar',first_name='bear')
        self.assertEqual(admin_user.email, 'supr@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superadmin)
        
class UserRegistrationTest(TestCase):

    def test_register_user(self):
        form = RegistrationForm(data={
            "first_name": "chowa",
            "last_name": "cross",
            "phone_number": "78562216365",
            "email": "cross@yahoo.com",
            "password": "manofsteel5",
            "confirm_password": "manofsteel5",
            })