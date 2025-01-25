from django.test import TestCase
from django.urls import reverse, resolve
from tweeter import views


class TestUrls(TestCase):
    def test_home_url_resolve(self):
        url = reverse('tweeter:home')
        self.assertEqual(resolve(url).func, views.home)
