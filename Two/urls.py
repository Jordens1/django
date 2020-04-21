#/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.urls import path
from . import views

urlpatterns = [
    path( 'two/', views.two ),
    path('get/', views.get),
    path( 'add/', views.add  ),
    path( 'addpersons/', views.add_persons),
    path( 'getpersons/', views.get_person ),
    path( 'getanimals/', views.get_animal, name = 'te'),

]

