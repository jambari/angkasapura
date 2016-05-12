from django.contrib import admin
from .models import Magnetbumi
# Register your models here.

class MagnetbumiAdmin(admin.ModelAdmin):
    list_display = ['tanggal','komponen', 'created', 'updated']
    search_fields = ['tanggal', 'created', 'komponen']

admin.site.register(Magnetbumi, MagnetbumiAdmin)
