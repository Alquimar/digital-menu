from django.contrib import admin
from digital_menu.establishment.models import Establishment


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    fields = ('user', 'name', 'phone', 'email', 'instagram', 'facebook', 'address', 'logo', 'active')
    list_display = ('name', 'phone', 'email', 'active')
    search_fields = ['name', 'email']
    list_filter = ('active',)
    exclude = ['slug']
