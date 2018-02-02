from django.contrib import admin
from . import models


class SecretAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'expired', 'expire_count',
        'expire_max_count', 'created', 'modified']
    readonly_fields = ['id', 'expired', 'expire_count']
    list_filter = ['expired']


admin.site.register(models.Secret, SecretAdmin)
