from django.urls import path
from . import views

app_name = "user"


urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/create/', views.create_user, name='create_user'),
    path('login/', views.login_view, name='login'),
    path('login/create/', views.login_create, name='login_create'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:id>/', views.profile, name='user_profile'),
    path('profile/<int:id>/update/', views.profile, name='update_profile'),
    path('follow/<int:id>/', views.toggle_follow, name='toggle_follow'),
]
