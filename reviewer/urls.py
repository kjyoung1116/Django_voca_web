from django.urls import path
from . import views

app_name = 'reviewer'

urlpatterns = [

    path('', views.index, name='index'),
    path('create/', views.reviewer_create, name='reviewer_create'),
    path('my_reviewers', views.my_reviewers, name='my_reviewers'),
]
