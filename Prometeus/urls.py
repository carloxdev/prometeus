# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf import settings
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls.static import static

from django.contrib import admin


urlpatterns = [
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^admin/', admin.site.urls),

    url(r'', include('editorial.urls', namespace="editorial")),
    url(r'', include('home.urls', namespace="home")),
    url(r'', include('labor.urls', namespace="labor")),
    url(r'', include('management.urls', namespace="management")),
    url(r'', include('payroll.urls', namespace="payroll")),
    url(r'', include('security.urls', namespace="security")),

    url(r'api/', include('payroll.urls_rest', namespace="api-payroll")),
    url(r'api/', include('social.urls_rest', namespace="api-social")),
]


if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
