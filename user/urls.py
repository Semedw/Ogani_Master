from django.urls import path

from django.contrib.auth import views as auth_views

from user.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('succes/', succes, name='succes'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')

]