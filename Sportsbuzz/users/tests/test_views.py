from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from users.models import User, Profile


class TestViews(TestCase):

    def setUp(self):
        self.user = {
            "username": "user",
            "email": "user@gmail.com",
            "password1": "password@123",
            "password2": "password@123"
        }

    def test_should_show_register_page(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_should_show_login_page(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_should_signup_user(self):

        response = self.client.post(reverse("register"), self.user)
        self.assertEqual(response.status_code, 302)

    def test_should_not_signup_user_with_taken_username(self):

        self.client.post(reverse("register"), self.user)
        response = self.client.post(reverse("register"), self.user)
        self.assertEqual(response.status_code, 302)

        storage = get_messages(response.wsgi_request)

        self.assertIn("That username is taken",
                      list(map(lambda x: x.message, storage)))

    def test_should_not_signup_user_with_taken_email(self):
        self.user = {
            "username": "user1",
            "email": "user1@gmail.com",
            "password1": "password@123",
            "password2": "password@123"
        }
        self.user2 = {
            "username": "user2",
            "email": "user1@gmail.com",
            "password1": "password@123",
            "password2": "password@123"
        }

        self.client.post(reverse("register"), self.user)
        response = self.client.post(reverse("register"), self.user2)
        self.assertEqual(response.status_code, 302)

        storage = get_messages(response.wsgi_request)
        self.assertIn("That email is taken",
                      list(map(lambda x: x.message, storage)))

    def test_should_login_successfully(self):
        user = User.objects.create_user(
            username='username', email='email@app.com')
        user.set_password('password12!')
        user.is_email_verified = True
        user.save()

        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!'
        })
        self.assertEquals(response.status_code, 302)

        storage = get_messages(response.wsgi_request)

        self.assertIn('You are now logged in!!',
                      list(map(lambda x: x.message, storage)))

    def test_should_not_login_with_invalid_password(self):
        user = User.objects.create_user(
            username='username', email='email@app.com')
        user.set_password('password12!')
        user.is_email_verified = True
        user.save()

        response = self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password12!32'
        })
        self.assertEquals(response.status_code, 302)

        storage = get_messages(response.wsgi_request)

        self.assertIn("Invalid Credentials",
                      list(map(lambda x: x.message, storage)))

    def test_should_show_change_password_page(self):
        user = User.objects.create_user(
            username='username', email='user@gmail.com', password='password@1234')

        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password@1234'
        })
        response = self.client.get(reverse('change_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_change.html')

    def test_should_user_change_password(self):
        user = User.objects.create_user(
            username='username', email='user@gmail.com', password='password@1234')

        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password@1234'
        })

        response = self.client.post(reverse("change_password"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/password_change.html')

        self.client.post(reverse("change_password"), {
            'old_password': 'password@1234',
            'new_password1': 'testuser@1234',
            'new_password2': 'testuser@1234'
        })

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

        storage = get_messages(response.wsgi_request)
        self.assertIn('Your password was successfully updated!',
                      list(map(lambda x: x.message, storage)))

    def test_should_show_user_profile_page(self):

        user = User.objects.create_user(
            username='username', email='user@gmail.com', password='password@1234')

        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password@1234'
        })


        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')


    def test_should_user_update_profile(self):
        user = User.objects.create_user(
            username='username', email='user@gmail.com', password='password@1234')

        self.client.post(reverse("login"), {
            'username': user.username,
            'password': 'password@1234'
        })

        response = self.client.post(reverse('profile'), {
            'username': 'test111',
            'email': 'test111@gmail.com'
        })
        self.assertEquals(response.status_code, 302)

        storage = get_messages(response.wsgi_request)
        for i in storage:
            print(i)
        self.assertIn('Your account has been updated!',
                      list(map(lambda x: x.message, storage)))