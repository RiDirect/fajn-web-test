from django.contrib import admin
from . models import Produkt,Kategorie,Objekt,TypObjektu
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ("id","name","objekt","typobjektu","description","cena","dostupnost")
    list_display_links=("name","description","id")
    list_filter = ("objekt","typobjektu")
admin.site.register(Produkt,ListingAdmin)

class ListingKategorie(admin.ModelAdmin):
    list_display=("name","description")
admin.site.register(Kategorie,ListingKategorie)




class ListingObjekt(admin.ModelAdmin):
    list_display=("name","description")
admin.site.register(Objekt,ListingObjekt)

class ListingTypObjektu(admin.ModelAdmin):
    list_display=("name","objekt","description")
admin.site.register(TypObjektu,ListingTypObjektu)