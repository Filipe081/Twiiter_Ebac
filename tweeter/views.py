from django.http import Http404
from django.shortcuts import render, redirect
from .models import Tweet
from django.urls import reverse
from users.forms.tweet_form import TweetForm
from django.core.paginator import Paginator
from utils.pagination import make_pagination_range
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm



import os



import os


PER_PAGE = os.environ.get('PER_PAGE', 5)


def home(request):
    if not request.user.is_authenticated:
        return redirect('user:login')
    tweets = Tweet.objects.all().order_by("-id")
    users = User.objects.all().order_by("-id")
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    paginator = Paginator(tweets, PER_PAGE)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        4,
        int(current_page)
    )

    create_tweet = request.POST.get('create_tweet', None)
    form = TweetForm(create_tweet)

    create_comment = request.POST.get('create_comment', None)
    comment_form = CommentForm(create_comment)
    return render(request, 'tweeter/pages/home.html', context={
        "tweets": page_obj,
        "form": form,
        'users': users,
        "pagination_range": pagination_range,
        "current_page": int(current_page),
        "user": request.user,
        'comment_form': comment_form,
    })


@login_required(login_url='user:login', redirect_field_name='next')
def create_tweet(request):
    form = TweetForm(request.POST or None)
    if form.is_valid():
        tweet = form.save(commit=False)
        tweet.user = request.user
        tweet.save()
        messages.success(request, 'Your tweet was created!')
        return redirect(reverse('tweeter:home'))


    if not request.POST:
        return redirect(reverse('tweeter:home'))

    return redirect(reverse('tweeter:home'))



@login_required(login_url='user:login', redirect_field_name='next')
def edit_tweet(request, id):
    users = User.objects.all()
    tweet = Tweet.objects.filter(user=request.user, id=id).first()
    if not tweet:
        raise Http404()

    form = TweetForm(request.POST or None, instance=tweet)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your tweet was updated successfully!')
        return redirect(reverse('tweeter:home'))

    return render(request, 'tweeter/pages/tweet_edit.html', {
        'form': form,
        'tweet': tweet,
        'users': users,
    })


@login_required(login_url='user:login', redirect_field_name='next')
def delete_tweet(request):
    if not request.POST:
        return redirect(reverse('tweeter:home'))
    id = request.POST.get('id')
    tweet = Tweet.objects.filter(
        user=request.user,
        id=id).first()

    if not tweet:
        raise Http404()
    tweet.delete()
    messages.success(request, 'your tweet was deleted!')
    return redirect(reverse('tweeter:home'))


@login_required(login_url='user:login', redirect_field_name='next')
def like_tweet(request, id):
    tweet = Tweet.objects.get(id=id)
    if request.user in tweet.likes.all():
        tweet.likes.remove(request.user)
    else:
        tweet.likes.add(request.user)
    tweet.save()
    return redirect(reverse('tweeter:home'))


@login_required(login_url='user:login', redirect_field_name='next')
def comment_tweet(request, id):
    tweet = Tweet.objects.get(id=id)
    user = request.user
    if not tweet:
        raise Http404()

    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.autor = user.profile
        comment.tweet = tweet
        comment.save()
        return redirect(reverse('tweeter:home'))

    return redirect(reverse('tweeter:home'))
