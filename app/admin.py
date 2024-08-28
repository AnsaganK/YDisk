from django.contrib import admin

from app.models import Resource


@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ['name', 'user__username', 'public_url']
    list_filter = ['user']