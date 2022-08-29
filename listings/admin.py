from django.contrib import admin
from . models import Produkt
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id","description","cena","dostupnost")
    list_display_links=("description",)
admin.site.register(Produkt,ListingAdmin)