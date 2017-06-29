# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url
from django.contrib.auth.views import LogoutView


# Own's Libraries
from .views import Login
from .views import Profile
from .views import ProfilePassword
from .views import ProfilePasswordSuccess
from .views import UserList
from .views import UserAdd
from .views import UserAddSuccess
from .views import UserEdit
from .views import UserPermissions
from .views import UserPassword
from .views import UserPasswordSuccess

urlpatterns = [
    url(r'^$', Login.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^profile/(?P<_pk>\d+)/$', Profile.as_view(), name="profile"),
    url(r'^profile/(?P<_pk>\d+)/password/$', ProfilePassword.as_view(), name="profile_password"),
    url(r'^profile/password/success/$', ProfilePasswordSuccess.as_view(), name="profile_password_success"),
    url(r'^users/$', UserList.as_view(), name="user_list"),
    url(r'^users/add/$', UserAdd.as_view(), name="user_add"),
    url(r'^users/add/success/$', UserAddSuccess.as_view(), name="user_add_success"),
    url(r'^users/(?P<_pk>\d+)/edit/$', UserEdit.as_view(), name="user_edit"),
    url(r'^users/(?P<_pk>\d+)/permissions/$', UserPermissions.as_view(), name="user_permissions"),
    url(r'^users/(?P<_pk>\d+)/password/$', UserPassword.as_view(), name="user_password"),
    url(r'^users/password/success/$', UserPasswordSuccess.as_view(), name="user_password_success"),
]
