from django.urls import path
from . import views

app_name = 'reviewer'

urlpatterns = [

    path('', views.index, name='index'),
    path('delete/<str:plan_name>', views.plan_delete, name='plan_delete'),
    path('create', views.reviewer_create, name='reviewer_create'),
    path('my_reviewers', views.my_reviewers, name='reviewer_current'),
    path("plan_detail/<str:user>/<str:plan_name>/",views.reviewer_plan_detail.as_view(),name="reviewer_plan_detail"),
    path("new_card",views.new_card.as_view(),name="new_card"),
    path("update_card/<int:pk>",views.update_card.as_view(),name="update_card"),
    path("box/<str:user>/<str:plan_name>/<str:review_date>", views.box_view.as_view(),name="box"),
]




