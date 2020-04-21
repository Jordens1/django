#/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.urls import path, re_path
from . import views

urlpatterns = [
    path('in/', views.index, name = 'test1' ),
    path( 'info/', views.getInfo, name='test2' ),
    path( 'jicheng/', views.jicheng, name='test3' ),
    re_path(r'^$', views.jicheng, name=''),
    path( 's/', views.jicheng, name='sec'),
    path( 'have/', views.have_request, name='sec2'),
]














