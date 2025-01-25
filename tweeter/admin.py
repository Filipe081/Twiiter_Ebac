from django.contrib import admin
from tweeter.models import Tweet


class TweetModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Tweet

# Register your models here.


admin.site.register(Tweet, TweetModelAdmin)
