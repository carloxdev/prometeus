# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

# Own's Libraries
from .views import Login

from .views import PasswordResetRequest
from .views import PasswordResetMessage
from .views import PasswordResetConfirm
from .views import PasswordResetDone

from .views import UserList
from .views import UserListExport
from .views import UserAdd
from .views import UserEdit
from .views import UserProfile
from .views import UserPassword

from .views import Profile
from .views import ProfilePassword
from .views import ProfilePasswordDone

from .views import UserPermissions


urlpatterns = [
    url(r'^login/$', Login.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),

    url(r'^password/reset/request/$', PasswordResetRequest.as_view(), name="password_reset_request"),
    url(r'^password/reset/(?P<_pk>\d+)/message/$', PasswordResetMessage.as_view(), name="password_reset_message"),
    url(r'^password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordResetConfirm.as_view(), name='password_reset_confirm'),
    url(r'^password/reset/done/$',
        PasswordResetDone.as_view(), name='password_reset_done'),

    url(r'^users/$', UserList.as_view(), name="user_list"),
    url(r'^users/export/$', UserListExport.as_view(), name="user_list_export"),

    url(r'^users/add/$', UserAdd.as_view(), name="user_add"),
    url(r'^users/(?P<_pk>\d+)/edit/$', UserEdit.as_view(), name="user_edit"),
    url(r'^users/(?P<_pk>\d+)/profile/$', UserProfile.as_view(), name="user_profile"),
    url(r'^users/(?P<_pk>\d+)/password/$', UserPassword.as_view(), name="user_password"),

    url(r'^profile/(?P<_pk>\d+)/$', Profile.as_view(), name="profile"),
    url(r'^profile/(?P<_pk>\d+)/password/$', ProfilePassword.as_view(), name="profile_password"),
    url(r'^profile/password/done/$', ProfilePasswordDone.as_view(), name="profile_password_done"),

    url(r'^users/(?P<_pk>\d+)/permissions/$', UserPermissions.as_view(), name="user_permissions"),


]
