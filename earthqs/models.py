from django.db import models
from django.utils import timezone
#from kantor.pegawais.models import Pegawai

# Create your models here.
MAG_CHOICES = (
    ('M','M'),
    ('MSH','MSH'),
    ('Mw', 'Mw'),
    ('Mwp', 'Mwp'),
    ('Ms', 'Ms'),
    ('MLv', 'MLv'),
)

IMPULSE_CHOICES = (
    ('IP', 'IP'),
    ('eP', 'eP'),
)


FIRST_CHOICES = (
    ('CNE', 'CNE'),
    ('CNW', 'CNW'),
    ('CSE', 'CSE'),
    ('CSW', 'CSW'),
    ('DNE', 'DNE'),
    ('DNW',' DNW'),
    ('DSE', 'DSE'),
    ('DSW', 'DSW'),
)

TIPE_CHOICES = (('local','local'),('Tele','Tele'),)

DIRASAKAN_CHOICES = (
    ('Tidak Dirasakan', 'Tidak Dirasakan'),
    ('Dirasakan', 'Dirasakan'),
)



class PhaseReportSheet(models.Model):
    tanggal = models.DateField()
    impulse = models.CharField(max_length=2, choices=IMPULSE_CHOICES, default='IP', blank=True)
    p_arrival = models.TimeField(blank=True)
    s_arrival = models.TimeField(blank=True)
    first_motion = models.CharField(max_length=3, choices=FIRST_CHOICES, default='CNE', blank=True)
    komponen_Z = models.FloatField(blank=True)
    komponen_NS = models.FloatField(blank=True)
    komponen_EW = models.FloatField(blank=True)
    a_maksimum = models.FloatField(blank=True)
    Periode = models.FloatField(blank=True)
    Tipe = models.CharField(max_length=2,blank=True, choices=TIPE_CHOICES, default='local')
    Distance = models.FloatField(blank=True)
    magnitudo_durasi = models.FloatField(blank=True)
    origin_time = models.TimeField()
    lintang = models.FloatField(default=0.0)
    bujur = models.FloatField(default=0.0)
    kedalaman = models.IntegerField(default=10)
    magnitudo = models.FloatField(default=0.0)
    tipe_magnitudo = models.CharField(max_length=5, choices=MAG_CHOICES, default='M')
    dirasakan = models.CharField(max_length=50, blank=True, choices=DIRASAKAN_CHOICES, default='Tidak Dirasakan')
    skala_mmi = models.CharField(help_text="Jika Gempa Dirasakan", blank=True, max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    #inisial = models.ForeignKey(Pegawai, on_delete=models.CASCADE)


    def __str__(self):
        return self.tanggal

    class Meta:
        ordering = ['tanggal']
