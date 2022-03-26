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

from myadmin.views import index, user, product

urlpatterns = [
    # homepage
    path('', index.index, name='mAD_index'),

    # user urls
    path('user/', user.show, name='mAD_user'),
    path('user/add', user.add, name='mAD_add'),
    path('user/insert', user.insert, name='mAD_insert'),
    path('user/del/<int:u_id>', user.delete, name='mAD_del'),
    path('user/recovery/<int:u_id>', user.recovery, name='mAD_rec'),
    path('user/edit/<int:u_id>', user.edit, name='mAD_edit'),
    path('user/update/<int:u_id>', user.updated, name='mAD_update'),

    # product
    path('product/', product.show_all, name='mAD_p_show'),
    path('product/view/<int:p_id>', product.show_details, name='mAD_p_view'),

    # Sign in
    path('signin/', index.signin_form, name='mAD_signin'),
    path('dosignin/', index.do_signin, name='mAD_dosignin'),
    path('signout/', index.sign_out, name='mAD_signout'),
    path('signup/', index.signup, name='mAD_signup'),
    path('signupcheck/', index.signup_check, name='mAD_signupcheck'),
]
