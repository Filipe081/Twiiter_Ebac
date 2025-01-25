from django.urls import path
from . import views

app_name = "tweeter"


urlpatterns = [
    # home page with tweet list.
    path('', views.home, name="home"),
    path('tweet/create/', views.create_tweet, name="create_tweet"),
    path('tweet/delete/', views.delete_tweet, name="tweet_delete"),
    path('tweet/edit/<int:id>/', views.edit_tweet, name="tweet_edit"),
    path('tweet/like/<int:id>/', views.like_tweet, name="like_tweet"),
    path('tweet/comment/<int:id>/', views.comment_tweet, name="comment_tweet"),
]
