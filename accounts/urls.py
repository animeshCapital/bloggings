from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.login_page, name='login'),
    path('profile/edit/', views.profile_edit, name='profile_edit'),
    path('profile/Change-password/', views.change_password, name='change_password'),
    path('logout', views.logout_page, name='logout')
]