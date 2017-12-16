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
        r'^incidences/pending/$',
        IncidentListPending.as_view(),
        name="incident_list_pending"
    ),
    url(
        r'^incidences/all/$',
        IncidentListAll.as_view(),
        name="incident_list_all"
    ),
    url(
        r'^incidences/admin/pending/$',
        IncidentListAdminPending.as_view(),
        name="incident_list_pending"
    ),
    url(
        r'^incidences/admin/all/$',
        IncidentListAdminAll.as_view(),
        name="incident_list_all"
    ),
    url(
        r'^incidences/add/$',
        IncidentAdd.as_view(),
        name="incident_add"
    ),
    url(
        r'^incidences/add/success/$',
        IncidentAddSuccess.as_view(),
        name="incident_add_success"
    ),
    url(
        r'^incidences/(?P<_pk>\d+)/view/$',
        IncidentView.as_view(),
        name="incident_view"
    ),
    url(
        r'^incidences/(?P<_pk>\d+)/edit/$',
        IncidentEdit.as_view(),
        name="incident_edit"
    ),
    url(
        r'^incidences/(?P<_pk>\d+)/cancel/$',
        IncidentCancel.as_view(),
        name="incident_cancel"
    ),
]
