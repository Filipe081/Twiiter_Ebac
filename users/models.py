from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(
        User, related_name='following', blank=True)
    birth_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def follow(self, user):
        return self.followers.add(user)

    def unfollow(self, user):
        return self.followers.remove(user)

    def is_following(self, user):
        return self.followers.filter(id=user.id).exists()
