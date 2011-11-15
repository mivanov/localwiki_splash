from django.contrib import admin

from models import LicenseAgreement

class LicenseAgreementAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'email')
    readonly_fields = ('signature',)

admin.site.register(LicenseAgreement, LicenseAgreementAdmin)