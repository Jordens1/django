"""xishi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from APP import views
from django.contrib import admin

from django.urls import include, path



app_name = 'polls'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', views.index, name='in'),
    path( 'detail/<int:question_id>/', views.details, name='in' ),

    path( 'html/', views.test, name ='test'),
    path( '', views.index, name='in' ),
    # ex: /5/
    path( '<int:question_id>/', views.detail, name='detail' ),
    # ex: /5/results/
    path( '<int:question_id>/results/', views.results, name='results' ),
    # ex: /5/vote/
    path( '<int:question_id>/vote/', views.vote, name='vote' ),
    path( 'in/', views.temindex, name='a' ),
    path( 'two/', include('Two.urls'), name='b' ),
    path( 'thr/', include( 'Three.urls' ), name='sec1' ),
    # path( 'fan/', include( 'Three.urls') , name='sec2'),

    path('four/', include('Four.urls', namespace= 'fou')),
    path('five/', include('Five.urls', namespace= 'five')),


]











