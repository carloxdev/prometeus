# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import IncidentListPending
from .views import IncidentListAll
from .views import IncidentListAdminPending
from .views import IncidentListAdminAll
from .views import IncidentAdd
from .views import IncidentAddSuccess
from .views import IncidentView
from .views import IncidentEdit
from .views import IncidentCancel


urlpatterns = [
    url(
        r'^incidents/pending/$',
        IncidentListPending.as_view(),
        name="incident_list_pending"
    ),
    url(
        r'^incidents/all/$',
        IncidentListAll.as_view(),
        name="incident_list_all"
    ),
    url(
        r'^incidents/admin/pending/$',
        IncidentListAdminPending.as_view(),
        name="incident_list_admin_pending"
    ),
    url(
        r'^incidents/admin/all/$',
        IncidentListAdminAll.as_view(),
        name="incident_list_admin_all"
    ),
    url(
        r'^incidents/add/$',
        IncidentAdd.as_view(),
        name="incident_add"
    ),
    url(
        r'^incidents/add/success/$',
        IncidentAddSuccess.as_view(),
        name="incident_add_success"
    ),
    url(
        r'^incidents/(?P<pk>\d+)/view/$',
        IncidentView.as_view(),
        name="incident_view"
    ),
    url(
        r'^incidents/(?P<pk>\d+)/edit/$',
        IncidentEdit.as_view(),
        name="incident_edit"
    ),
    url(
        r'^incidents/(?P<pk>\d+)/cancel/$',
        IncidentCancel.as_view(),
        name="incident_cancel"
    ),
]
