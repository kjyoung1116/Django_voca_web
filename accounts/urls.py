from django.conf import settings
from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from accounts import views


urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    
]
