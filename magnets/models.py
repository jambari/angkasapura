from django.db import models
from django.utils import timezone
# Create your models here.

KOMPONEN = (
    ('komponen x', 'komponen x'),
    ('komponen y', 'komponen y'),
    ('Komponen z', 'komponen z'),
    ('horizontal', 'horizontal'),
    ('komponen f', 'komponen f'),
    ('deklinasi', 'deklinasi'),
    ('inklinasi', 'inklinasi'),
)

class Magnetbumi(models.Model):
    tanggal = models.DateField()
    komponen = models.CharField(max_length=100, choices=KOMPONEN, default='komponen x')
    jam_01 = models.FloatField(default=0.0)
    jam_02 = models.FloatField(default=0.0)
    jam_03 = models.FloatField(default=0.0)
    jam_04 = models.FloatField(default=0.0)
    jam_05 = models.FloatField(default=0.0)
    jam_06 = models.FloatField(default=0.0)
    jam_07 = models.FloatField(default=0.0)
    jam_08 = models.FloatField(default=0.0)
    jam_09 = models.FloatField(default=0.0)
    jam_10 = models.FloatField(default=0.0)
    jam_11 = models.FloatField(default=0.0)
    jam_12 = models.FloatField(default=0.0)
    jam_13 = models.FloatField(default=0.0)
    jam_14 = models.FloatField(default=0.0)
    jam_15 = models.FloatField(default=0.0)
    jam_16 = models.FloatField(default=0.0)
    jam_17 = models.FloatField(default=0.0)
    jam_18 = models.FloatField(default=0.0)
    jam_19 = models.FloatField(default=0.0)
    jam_20 = models.FloatField(default=0.0)
    jam_21 = models.FloatField(default=0.0)
    jam_22 = models.FloatField(default=0.0)
    jam_23 = models.FloatField(default=0.0)
    jam_24 = models.FloatField(default=0.0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.jam_01

    class Meta:
        ordering = ['tanggal']
        verbose_name_plural = 'Magnetbumi'


