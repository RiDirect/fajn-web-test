from django.shortcuts import render
from . import models
from listings import urls
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


# Create your views here.
def index(request):
    listings = models.Produkt.objects.all()

    paginator = Paginator(listings,20)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)
    context = {
            'listings': paged_listings,
           

    }
    return render(request,'listings.html',context)