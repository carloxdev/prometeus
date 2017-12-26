# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import IncidentListView
from .views import IncidentListEdit
from .views import IncidentAdd
from .views import IncidentAddSuccess
from .views import IncidentAddEvidence
from .views import IncidentView
from .views import IncidentEdit
from .views import IncidentCancel


urlpatterns = [
    url(
        r'^incidents/pending/$',
        IncidentListView.as_view(), {'_status': 'pending'},
        name="incident_list_pending"
    ),
    url(
        r'^incidents/all/$',
        IncidentListView.as_view(), {'_status': 'all'},
        name="incident_list_all"
    ),
    url(
        r'^incidents/admin/pending/$',
        IncidentListEdit.as_view(), {'_status': 'pending'},
        name="incident_list_admin_pending"
    ),
    url(
        r'^incidents/admin/all/$',
        IncidentListEdit.as_view(), {'_status': 'all'},
        name="incident_list_admin_all"
    ),
    url(
        r'^incidents/add/$',
        IncidentAdd.as_view(),
        name="incident_add"
    ),
    url(
        r'^incidents/(?P<pk>\d+)/evidence/add/$',
        IncidentAddEvidence.as_view(),
        name="incident_add_evidence"
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
