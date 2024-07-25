from django.contrib import admin
from .models import Guest


class GuestAdmin(admin.ModelAdmin):
    list_display = ('name', 'confirmed', 'confirmed_at')
    list_filter = ('confirmed', 'name')
    search_fields = ('name',)

admin.site.register(Guest, GuestAdmin)


