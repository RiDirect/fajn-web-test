from django.shortcuts import render
from . import models
from listings import urls
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# listings = models.Produkt.objects.filter(typobjektu__name__startswith="Ča")
# Create your views here.
def index(request):
    
    return render(request,'index.html')
def container(request):
        
        
     return render(request,'container.html')

def listing(request,listing_id):
     listing = models.Produkt.objects.get(id=listing_id)
     context = {
            'listing': listing
           

    }
     return render(request,'listing.html',context)

def calounene_postele(request):
     listings = models.Produkt.objects.filter(sub_category__name__icontains="Čalouněné")

     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     context = {
               'listings': paged_listings,
               

     }
     return render(request,'loznice/calounene_postele.html',context)

def postele_z_masivu(request):
     listings = models.Produkt.objects.filter(sub_category__name__icontains="masivu")

     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     context = {
               'listings': paged_listings,
               

     }
     return render(request,'loznice/postele_z_masivu.html',context)

def valendy(request):
     listings = models.Produkt.objects.filter(sub_category__name__icontains="Válend")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     context = {
               'listings': paged_listings,
               

     }
     return render(request,'loznice/valendy.html',context)

def postelove_ramy(request):
     listings = models.Produkt.objects.filter(sub_category__name="Postelové rámy")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     context = {
               'listings': paged_listings,
               

     }
     return render(request,'loznice/postelove_ramy.html',context)

def category_listings(request):  

     listings = models.Produkt.objects.all()
     types = models.Sub_sub_Category.objects.all()

     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     context = {
               'listings': paged_listings,
               "types": types,
               
               

     }
     return render(request,'category_listings.html',context)

# def listing(request,listing_id):
#         listing = models.Produkt.objects.get(pk=listing_id)

#         context = {
#                 "listing": listing
#         }

#         return render(request, 'listing.html',context)
        
        