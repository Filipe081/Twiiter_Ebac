from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LogInForm, RegisterForm
from .forms import ProfileUpdateForm, UserUpdateForm
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tweeter.models import Tweet


def login_view(request):
    login_data = request.session.get('login_data', None)
    form = LogInForm(login_data)
    return render(request, 'user/pages/login.html', context={
        'form': form,
        'form_action': reverse('user:login_create'),
        'is_login': True
    })


def login_create(request):
    if not request.POST:
        raise Http404()
    form = LogInForm(request.POST)
    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('usuario', ''),
            password=form.cleaned_data.get('senha', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Login successful')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('user:login')
    else:
        messages.error(request, 'Error to validate form data')

    return redirect(reverse('tweeter:home'))


def register(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'user/pages/register.html', context={
        'form': form,
        'form_action': reverse('user:create_user'),
    })


def create_user(request):
    if not request.POST:
        raise Http404
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Usuário registrado com sucesso!')
        del request.session['register_form_data']

    return redirect('user:register')


@login_required(login_url='user:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('user:login'))

    if request.POST.get('username') != request.user.username:
        return redirect(reverse('user:login'))

    logout(request)
    return redirect(reverse('user:login'))


@login_required(login_url='user:login', redirect_field_name='next')
def profile(request, id):
    user = User.objects.get(id=id)
    tweets = Tweet.objects.filter(user=user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect(reverse('user:user_profile', args=[user.id]))
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
        'user': user,
        'is_self': request.user.id == user.id,
        'tweets': tweets,
    }
    if request.user.id == user.id:
        return render(request, 'user/pages/profile.html', context)
    else:
        return render(request, 'user/pages/profile.html', context={
            'user': user,
            'tweets': tweets
        })


@login_required(login_url='user:login', redirect_field_name='next')
def toggle_follow(request, id):
    user_to_follow = User.objects.get(id=id)
    if request.user.profile.is_following(user_to_follow):
        request.user.profile.unfollow(user_to_follow)
    else:
        request.user.profile.follow(user_to_follow)
    return redirect(reverse('user:user_profile', args=[id]))
