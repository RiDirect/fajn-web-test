from django.shortcuts import render
from . import models
from listings import urls
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# listings = models.Produkt.objects.filter(typobjektu__name__startswith="Ča")
# Create your views here.

#TODO make filter to each one main category
def index(request):
    
    return render(request,'index.html')
def cart(request):
     return render(request,'cart/cart.html')
def container(request):
        
        
     return render(request,'container.html')
def prodejny_vydejny(request):
     return render(request,'dev/prodejny_vydejny.html')
def zakladni_informace(request):
     return render(request,'dev/zakladni_informace.html')
def postele(request,slug):
     listing = models.Produkt.objects.all()
     context = {
            'listing': listing
           

    }
     return render(request,'listing.html',context)
def listing(request,listing_id):
     listing = models.Produkt.objects.get(id=listing_id)
     context = {
            'listing': listing
           

    }
     return render(request,'listing.html',context)
def postele_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)
def postele_z_masivu_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def calounene_postele_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)
def postelove_ramy_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def skrine_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)
def valendy_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def komody_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def nocni_stolky_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def matrace_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def sedaci_soupravy_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def rohove_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def levne_sedaci_soupravy_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def kazdodenni_spanni_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def obyvaci_steny_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def ob_komody_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def tv_stolky_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def konferencni_stolky_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def kuchynske_linky_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def blokove_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def na_miru_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def sakypaky_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def jidelni_stolky_sety_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def jidelni_zidle_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def detsky_postele_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def caloun_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)
def poschodi_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def sestavy_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def detsky_zidle_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def kancelare_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def predsine_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def regaly_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def ostatni_zidle_details(request,slug):
     listing = models.Produkt.objects.get(slug=slug)
     context = {
            'listing': listing
           

    }
     return render(request,'detail_view.html',context)

def sedaci_soupravy(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name="sedaci_soupravy_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def rohove(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name="rohove_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def levne_sedaci_soupravy(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name="levne_sedaci_soupravy_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)


def obyvaci_steny(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name="obyvaci_steny_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)
def ob_komody(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "ob_komody_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def tv_stolky(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name="tv_stolky_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)
def konferencni_stolky(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name="konferencni_stolky_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)
def kazdodenni_spanni(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "kazdodenni_spanni_details"
     context = {
               'listings': paged_listings,
               "name":name
               

     }
     return render(request,'listing_view.html',context)

def sakypaky(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name="sakypaky_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def kuchynske_linky(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "kuchynske_linky_details"
     context = {
               'listings': paged_listings,
               "name": name
               
               

     }
     return render(request,'listing_view.html',context)

def blokove(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "blokove_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def na_miru(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "na_miru_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def jidelni_stolky_sety(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "jidelni_stolky_sety_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def jidelni_zidle(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "jidelni_zidle_details"
     context = {
               'listings': paged_listings,
               "name":name
               

     }
     return render(request,'listing_view.html',context)
def detsky_postele(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "detsky_postele_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def caloun(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "caloun_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def poschodi(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "poschodi_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def sestavy(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "sestavy_details"
     context = {
               'listings': paged_listings,
               "name":name
               

     }
     return render(request,'listing_view.html',context)

def detsky_zidle(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "detsky_zidle_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def kancelare(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "kancelare_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def predsine(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "predsine_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def regaly(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "regaly_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)

def ostatni_zidle(request):
     listings = models.Produkt.objects.all()
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "ostatni_zidle_details"
     context = {
               'listings': paged_listings,
               "name":name
               
               

     }
     return render(request,'listing_view.html',context)
def calounene_postele(request):
     listings = models.Produkt.objects.filter(sub_category__name__icontains="Čalouněné")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "calounene_postele_details"
     context = {
               'listings': paged_listings,
               "name" :name

     }
     return render(request,'listing_view.html',context)


def postele_z_masivu(request):
     listings = models.Produkt.objects.filter(sub_category__name__icontains="masivu")

     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "postele_z_masivu_details"
     context = {
               'listings': paged_listings,
               "name" : name
               

     }
     return render(request,'listing_view.html',context)

def valendy(request):
     listings = models.Produkt.objects.filter(sub_category__name__icontains="Válend")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "valendy_details"

     context = {
               'listings': paged_listings,
               "name" : name

     }
     return render(request,'listing_view.html',context)

def postelove_ramy(request):
     listings = models.Produkt.objects.filter(sub_category__name="Postelové rámy")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "postelove_ramy_details"
     context = {
               'listings': paged_listings,
               "name":name
               

     }
     return render(request,'listing_view.html',context)
def komody(request):
     listings = models.Produkt.objects.filter(category__name="Komody")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "komody_details"
     context = {
               'listings': paged_listings,
               "name":name,
               
               

     }
     return render(request,'listing_view.html',context)
def skrine(request):
     listings = models.Produkt.objects.filter(category__name="Skříně")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "skrine_details"
     context = {
               'listings': paged_listings,
               "name":name,
               
               

     }
     return render(request,'listing_view.html',context)

def nocní_stolky(request):
     listings = models.Produkt.objects.filter(category__name="Noční Stolky")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "nocni_stolky_details"
     context = {
               'listings': paged_listings,
               "name":name,
               
               

     }
     return render(request,'listing_view.html',context)
def matrace(request):
     listings = models.Produkt.objects.filter(category__name="Matrace")
     paginator = Paginator(listings,12)
     page = request.GET.get('page')
     paged_listings = paginator.get_page(page)
     name = "matrace_details"
     context = {
               'listings': paged_listings,
               "name":name,
               
               

     }
     return render(request,'listing_view.html',context)
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






#OUT OF PRODUCT VIEW, INTERNAL THINGS

def dev_kancelare(request):

     return render(request,'dev/dev-kancelare.html')

def dev_kuchyne(request):

     return render(request,'dev/dev-kuchyne.html')

def dev_nabytek(request):

     return render(request,'dev/dev-nabytek.html')

def dev_spotrebice(request):

     return render(request,'dev/dev-spotrebice.html')

def dev_spotrebice(request):

     return render(request,'dev/dev-spotrebice.html')

def developerske_projekty(request):

     return render(request,'dev/developerske-projekty.html')

# def listing(request,listing_id):
#         listing = models.Produkt.objects.get(pk=listing_id)

#         context = {
#                 "listing": listing
#         }

#         return render(request, 'listing.html',context)
