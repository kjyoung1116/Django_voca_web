from django.urls import path, re_path
from . import views

app_name = 'board'

urlpatterns = [
    path('', views.index, name='index'),
    re_path('K_SAT/page(?P<param>\d+)/$', views.K_SAT, name='K_SAT'),
    re_path('alphabet/page(?P<param>\d+)/$', views.alphabet, name='alphabet'),
    path('confusing', views.confusing, name='confusing'),
    path('elementary', views.elementary, name='elementary'),
    path('significance', views.significance, name='significance'),
    re_path('GRE/page(?P<param>\d+)/$', views.GRE, name='GRE'),
    path('practice', views.practice, name='practice'),
    path('learn_review', views.learn_review, name='learn_review'),

    re_path('K_SAT/(?P<param>\d+)/$', views.K_SATdetail, name='K_SATdetail'),
    re_path('GRE/(?P<param>\d+)/$', views.GRE_detail, name='GRE_detail'),
    re_path('elementary/(?P<param>\d+)/$', views.elementary_detail, name='elementary_detail'),
    re_path('alphabet/(?P<param>\d+)/$', views.alphabet_detail, name='alphabet_detail'),
    re_path('alphabet/list', views.alphabet, name='alphabet'),
    re_path('confusing/(?P<param>\d+)/$', views.confusing_detail, name='confusing_detail'),
    re_path('significance/(?P<param>\d+)/$', views.significance_detail, name='significance_detail'),    
    re_path('practice/(?P<param>\d+)/$', views.practice_detail, name='practice_detail'),

    
]
