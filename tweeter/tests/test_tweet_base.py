from django.test import TestCase  # type: ignore
from tweeter.models import Tweet, User


class TweetTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_author(
            self, first_name='John',
            last_name='Doe',
            username='test_user',
            email='test_email@example.com',
            password='test_password'):
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password)

    def make_tweet(self, content='Tis is a test for a tweet'):
        return Tweet.objects.create(user=self.make_author(),
                                    content=content)
