from django.contrib import admin
from .models import Pegawai
# Register your models here.

class PegawaiAdmin(admin.ModelAdmin):
    fields = ('nama', 'inisial')
    list_display = ('nama', 'inisial', 'created', 'updated')
    search_fields = ('nama', 'creatted', 'updated')
    list_filter = ('nama', 'inisial', 'created')

admin.site.register(Pegawai, PegawaiAdmin)