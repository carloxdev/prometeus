# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import IncidentList
from .views import IncidentAdd
from .views import IncidentAddSuccess
from .views import IncidentEdit


urlpatterns = [
    url(r'^incidences/$', IncidentList.as_view(), name="incident_list"),
    url(r'^incidences/add/$', IncidentAdd.as_view(), name="incident_add"),
    url(r'^incidences/add/success/$', IncidentAddSuccess.as_view(), name="incident_add_success"),
    url(r'^incidences/(?P<_pk>\d+)/edit/$', IncidentEdit.as_view(), name="incident_edit"),
]
