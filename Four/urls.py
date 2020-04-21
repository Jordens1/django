#/usr/bin/env python
# _*_ coding:utf-8 _*_

from django.urls import path, re_path
from . import views

app_name = 'Four'
urlpatterns = [
    re_path('^fir.*/', views.firf, name = 'firf'),
    path('sec/', views.sec, name = 'secf' ),
    path('login/', views.login, name ='login'),
    # path('set-cookie/', views.set_cookie, name = 'set-cookie' ),
    path('get-cookie/', views.get_cookie, name = 'get-cookie' ),
    path('set-cookie/', views.set_cookie, name = 'set-cookie' ),
    path('do_login/', views.do_login, name = 'do_login' ),
    path('do_loginout/', views.do_loginout, name = 'logout' ),
    path('do_inout/', views.do_inout, name = 'inout' ),
    path('mine/', views.mine, name = 'mine' ),
    path('register/', views.register, name = 'register' ),
    path('stu_register/', views.stu_register, name = 'stu_register' ),
]



