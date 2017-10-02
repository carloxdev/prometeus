# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url
# from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

# Own's Libraries
from .views import Login

from .views import PasswordRequest
from .views import PasswordMessage
from .views import PasswordConfirm
from .views import PasswordDone

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

    url(r'^password/request/$', PasswordRequest.as_view(), name="password_request"),
    url(r'^password/(?P<_pk>\d+)/message/$', PasswordMessage.as_view(), name="password_message"),
    url(r'^password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        PasswordConfirm.as_view(), name='password_confirm'),
    url(r'^password/done/$',
        PasswordDone.as_view(), name='password_done'),

    url(r'^users/$', UserList.as_view(), name="user_list"),
    url(r'^users/export/(?P<_query>.*)/$', UserListExport.as_view(), name="user_list_export"),
    url(r'^users/add/$', UserAdd.as_view(), name="user_add"),
    url(r'^users/(?P<_pk>\d+)/edit/$', UserEdit.as_view(), name="user_edit"),
    url(r'^users/(?P<_pk>\d+)/profile/$', UserProfile.as_view(), name="user_profile"),
    url(r'^users/(?P<_pk>\d+)/password/$', UserPassword.as_view(), name="user_password"),
    url(r'^users/(?P<_pk>\d+)/permissions/$', UserPermissions.as_view(), name="user_permissions"),

    url(r'^profile/(?P<_pk>\d+)/$', Profile.as_view(), name="profile"),
    url(r'^profile/(?P<_pk>\d+)/password/$', ProfilePassword.as_view(), name="profile_password"),
    url(r'^profile/password/done/$', ProfilePasswordDone.as_view(), name="profile_password_done"),

]
