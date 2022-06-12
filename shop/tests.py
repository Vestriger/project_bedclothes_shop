from django.test import TestCase


class RegistrationTestCase(TestCase):
    def test_registration(self):
        form_data = {'username': "testuser", "password1": "testuser1234", 'password2': "testuser1234"}
        response = self.client.post("/register/", data=form_data)
        self.assertEqual(response.status_code, 200)


class ProfileViewTestCase(TestCase):
    def test_login(self) -> None:
        form_data = {'username': "testuser", "password1": "testuser1234", 'password2': "testuser1234"}
        self.client.post("/login/", data=form_data)
