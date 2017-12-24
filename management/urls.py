# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import TaskList
# from .views import TaskVouchers
# from .views import TaskBenefits
# from .views import TaskIncidents


urlpatterns = [
    url(r'^tasks/$', TaskList.as_view(), name="task_list"),
]
