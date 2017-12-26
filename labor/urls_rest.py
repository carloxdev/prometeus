# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views_rest import IncidentEvidenceAPIView


urlpatterns = [
    url(
        r'^incidentevidence/$',
        IncidentEvidenceAPIView.as_view(),
        name="incidentevidence-add"
    ),
]
