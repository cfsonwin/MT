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
from myadmin.views import index, user
from django.urls import path

urlpatterns = [
    # homepage
    path('', index.index, name='mAD_index'),

    # user urls
    path('user/', user.show, name='mAD_user'),
    path('user/add', user.add, name='mAD_add'),
    path('user/insert', user.insert, name='mAD_insert'),
    path('user/del/<int:u_id>', user.delete, name='mAD_del'),
    path('user/edit/<int:u_id>', user.edit, name='mAD_edit'),
    path('user/update/<int:u_id>', user.update, name='mAD_update'),

    # Sign in
    path('signin/', index.signin, name='mAD_signin'),
]
