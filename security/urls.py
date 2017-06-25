# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url
from django.contrib.auth.views import LogoutView


# Own's Libraries
from .views import Login
from .views import Perfil
from .views import PerfilPassword
from .views import PerfilPasswordSuccess
from .views import UserList
from .views import UserAdd
from .views import UserAddSuccess
from .views import UserEdit
from .views import UserPassword
from .views import UserPasswordSuccess

urlpatterns = [
    url(r'^$', Login.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^perfil/(?P<_pk>\d+)/$', Perfil.as_view(), name="perfil"),
    url(r'^perfil/(?P<_pk>\d+)/password/$', PerfilPassword.as_view(), name="perfil_password"),
    url(r'^perfil/password/success/$', PerfilPasswordSuccess.as_view(), name="perfil_password_success"),
    url(r'^users/$', UserList.as_view(), name="user_list"),
    url(r'^users/add/$', UserAdd.as_view(), name="user_add"),
    url(r'^users/add/success/$', UserAddSuccess.as_view(), name="user_add_success"),
    url(r'^users/(?P<_pk>\d+)/edit/$', UserEdit.as_view(), name="user_edit"),
    url(r'^users/(?P<_pk>\d+)/password/$', UserPassword.as_view(), name="user_password"),
    url(r'^users/password/success/$', UserPasswordSuccess.as_view(), name="user_password_success"),
]
