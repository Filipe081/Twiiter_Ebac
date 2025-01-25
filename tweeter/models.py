from django.contrib.auth.models import User
from django.db import models
from tweeter.validators import validate_content
from users.models import Profile


class Tweet(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tweets')
    content = models.TextField(max_length=300, validators=[validate_content])
    contents = models.TextField(max_length=300, validators=[validate_content])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='liked_tweets')

    def __str__(self):
        return f'{self.user.username}: {self.contents[:50]}...'


class Comment(models.Model):
    tweet = models.ForeignKey(
        Tweet, on_delete=models.CASCADE, related_name='comments')
    autor = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='comments', null=True)
    content = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.autor.username if self.autor else "Unknown"} on {self.tweet}'  # noqa:E501
