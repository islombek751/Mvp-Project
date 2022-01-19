from django.contrib import admin

from API.models import Client, Driver, Order

# Register your models here.
admin.site.register(Driver)
admin.site.register(Client)

@admin.register(Order)
class MahallaAdmin(admin.ModelAdmin):
	list_display = ['id', 'status']