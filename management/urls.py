# -*- coding: utf-8 -*-

# Django's Libraries
from django.conf.urls import url

# Own's Libraries
from .views import EmailConfig
from .views import TaskList
# from .views import TaskVouchers
# from .views import TaskBenefits
# from .views import TaskIncidents


urlpatterns = [
    url(r'^email/$', EmailConfig.as_view(), name="email"),
    url(r'^tasks/$', TaskList.as_view(), name="task_list"),
    # url(r'^tasks/vouchers/$', TaskVouchers.as_view(), name="task_vouchers"),
    # url(r'^tasks/benefits/$', TaskBenefits.as_view(), name="task_benefits"),
    # url(r'^tasks/incidents/$', TaskIncidents.as_view(), name="task_incidents"),
]
