from django.db import models
from django.utils.translation import gettext_lazy as _

class Preference(models.TextChoices):
    LONG = 'ln', _('LONG')
    SHORT = 'sh', _('SHORT')
