from django.contrib import admin
from . models import Main_Category,Sub_Category,Sub_sub_Category,Produkt,Variants
# Register your models here.


class ListingProdukt(admin.ModelAdmin):
    list_display = ("name","main_category","category","price")
    list_display_links=("name","main_category","category","price")
admin.site.register(Produkt,ListingProdukt)

class Listing_main_category(admin.ModelAdmin):
    list_display=("name","description")
admin.site.register(Main_Category,Listing_main_category)

class Listing_sub_category(admin.ModelAdmin):
    list_display=("name","main_category","description")
    list_display_links=("name","main_category","description")
admin.site.register(Sub_Category,Listing_sub_category)

class Listing_sub_sub_category(admin.ModelAdmin):
    list_display= ("main_category","name","description","sub_category")
    list_display_links=("main_category","name","description","sub_category")
admin.site.register(Sub_sub_Category,Listing_sub_sub_category)
class Listing_variants(admin.ModelAdmin):
    list_display=("eanv","product_name","rozmery_sirka","rozmery_delka","barva")
    list_display_links=("eanv","product_name","rozmery_sirka","rozmery_delka","barva")
admin.site.register(Variants,Listing_variants)