from django.shortcuts import render
from . import models
from listings import urls
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# listings = models.Produkt.objects.filter(typobjektu__name__startswith="Ča")
# Create your views here.
def index(request):
    listings = models.Produkt.objects.all()

    paginator = Paginator(listings,12)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
            'listings': paged_listings,
           

    }
    return render(request,'listings.html',context)
def container(request):
        
        
     return render(request,'container.html')

def listing(request,listing_id):
     listing = models.Produkt.objects.get(id=listing_id)
     context = {
            'listing': listing
           

    }
     return render(request,'listing.html',context)

def listing_calounene_postele(request):
     listings = models.Produkt.objects.all()

     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     context = {
               'listings': paged_listings,
               

     }
     return render(request,'calounene_postele.html',context)

def listing_postele_z_masivu(request):
     listings = models.Produkt.objects.all()

     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     context = {
               'listings': paged_listings,
               

     }
     return render(request,'postele_z_masivu.html',context)

def category_listings(request):  

     listings = models.Produkt.objects.all()

     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     context = {
               'listings': paged_listings,
               

     }
     return render(request,'category_listings.html',context)

# def listing(request,listing_id):
#         listing = models.Produkt.objects.get(pk=listing_id)

#         context = {
#                 "listing": listing
#         }

#         return render(request, 'listing.html',context)
        
        