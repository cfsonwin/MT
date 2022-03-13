"""myboot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
from myadmin.views import index, user, product

urlpatterns = [
    # homepage
    path('', views.index, name='t0'),
    path('t1/', views.t1, name='t1'),
    path('t2/', views.t2, name='t2'),
    path('t3/', views.t3, name='t3'),
    path('t4/', views.t4, name='t4'),


]
