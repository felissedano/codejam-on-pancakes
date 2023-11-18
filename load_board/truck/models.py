from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Trucker(models.Model):
    class TruckType(models.TextChoices):
        VAN = 'VN', _('VAN')
        FLATBED = 'FB', _('FLATBED')
        REEFER = 'RF', _('REEFER')

    truckerid = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField





        




        