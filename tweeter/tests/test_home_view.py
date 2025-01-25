from django.urls import reverse, resolve  # type: ignore
from tweeter import views
from .test_tweet_base import TweetTestBase


class TestViews(TweetTestBase):
    def test_home_view_load_is_correct(self):
        view = resolve(reverse('tweeter:home'))
        self.assertIs(view.func, views.home)
