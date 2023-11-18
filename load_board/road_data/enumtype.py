from django.db import models
from django.utils.translation import gettext_lazy as _


class TruckType(models.TextChoices):
    VAN = 'VN', _('VAN')
    FLATBED = 'FB', _('FLATBED')
    REEFER = 'RF', _('REEFER')
    


class Preference(models.TextChoices):
    LONG = 'ln', _('LONG')
    SHORT = 'sh', _('SHORT')
