from django.contrib import admin
from .models import PhaseReportSheet

# Register your models here.

class PhaseReportSheetAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields' : ['tanggal']
        }),
        (
            'Parameter dari Jamstec dan WGSN', {
                'fields': ['impulse', 'p_arrival', 's_arrival', 'first_motion', 'komponen_Z',
                           'komponen_NS', 'komponen_EW', 'a_maksimum', 'Periode',
                           'Tipe', 'Distance', 'magnitudo_durasi']
            }
        ),
        (
            'Hasil Analisa Seiscomp3 or WGSNPlot', {
                'fields': ['origin_time', 'lintang', 'bujur', 'kedalaman',
                           'magnitudo', 'tipe_magnitudo',]
            }
        ),
        (
            None, {
                'fields': ['dirasakan', 'skala_MMI']
            }
        )
    ]

    list_display = ['tanggal','origin_time', 'lintang', 'bujur', 'kedalaman', 'magnitudo', 'created', 'updated']

admin.site.register(PhaseReportSheet, PhaseReportSheetAdmin)

