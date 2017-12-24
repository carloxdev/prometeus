# -*- coding: utf-8 -*-

# Django's Libraries
from django.core.mail import send_mail
from django.conf import settings

# Own's Libraries
from .models import VoucherConfig
from .models import IncidentConfig
from .models import BenefitConfig


class VoucherMail(object):

    @staticmethod
    def send(_type, _subject, _content):
        try:
            vconfig = VoucherConfig.objects.get(
                type=_type
            )

            if vconfig:
                send_mail(
                    _subject,
                    _content,
                    settings.DEFAULT_FROM_EMAIL,
                    [vconfig.email]
                )
        except Exception:
            pass


class IncidentMail(object):

    @staticmethod
    def send(_type, _subject, _content):
        try:
            iconfig = IncidentConfig.objects.get(
                type=_type
            )

            if iconfig:
                send_mail(
                    _subject,
                    _content,
                    settings.DEFAULT_FROM_EMAIL,
                    [iconfig.email]
                )
        except Exception:
            pass


class BenefittMail(object):

    @staticmethod
    def send(_type, _subject, _content):
        try:
            bconfig = BenefitConfig.objects.get(
                type=_type
            )

            if bconfig:
                send_mail(
                    _subject,
                    _content,
                    settings.DEFAULT_FROM_EMAIL,
                    [bconfig.email]
                )
        except Exception:
            pass
