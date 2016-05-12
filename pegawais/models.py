from django.db import models
from django.utils import timezone
# Create your models here.

class Pegawai(models.Model):
    inisial = models.CharField(max_length=5)
    nama = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    class Meta:
        ordering = ['nama']
        verbose_name_plural = "Pegawai"
