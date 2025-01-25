from .test_tweet_base import TweetTestBase


class TestTweetModel(TweetTestBase):
    def test_tweet_creation(self):
        tweet = self.make_tweet()
        self.assertIsNotNone(tweet)
        self.assertEqual(tweet.content, 'Tis is a test for a tweet')
        self.assertEqual(tweet.user.first_name, 'John')
        self.assertEqual(tweet.user.last_name, 'Doe')
        self.assertEqual(tweet.user.username, 'test_user')
