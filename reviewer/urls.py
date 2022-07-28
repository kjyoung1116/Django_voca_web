from django.urls import path
from . import views

app_name = 'reviewer'

urlpatterns = [

    path('', views.index, name='index'),
    path('create', views.reviewer_create, name='reviewer_create'),
    path('my_reviewers', views.my_reviewers, name='my_reviewers'),
    path("detail",views.reviewer_detail.as_view(),name="reviewer_detail"),
    path("new_card",views.new_card.as_view(),name="new_card"),
    path("update_card/<int:pk>",views.update_card.as_view(),name="update_card"),
]




