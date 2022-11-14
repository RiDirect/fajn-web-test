"""Nabtek URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name="listings"),
    path('listing/<int:listing_id>',views.listing,name="listing"),
    path('container',views.container,name="container"),
    path('postele',views.category_listings,name="postele"),
    path('loznice/postele/calounene_postele',views.calounene_postele,name="calounene_postele"),
    path('loznice/postele/postele_z_masivu',views.postele_z_masivu,name="postele_z_masivu"),
    path('loznice/postele/postelove_ramy',views.postelove_ramy,name="postelove_ramy"),
    path('loznice/valendy',views.valendy,name="valendy"),
    path('loznice/komody',views.komody,name="komody"),
    path('loznice/skrine',views.skrine,name="skrine"),
    path('loznice/nocni_stolky',views.nocní_stolky,name="nocni_stolky"),
    path('loznice/matrace',views.matrace,name="matrace"),
    path('obyvaci_pokoj/sedaci_soupravy',views.sedaci_soupravy,name="sedaci_soupravy"),
    path('obyvaci_pokoj/sedaci_soupravy/rohove',views.rohove,name="rohove"),
    path('obyvaci_pokoj/sedaci_soupravy/levne_sedaci_soupravy',views.levne_sedaci_soupravy,name="levne_sedaci_soupravy"),
    path('obyvaci_pokoj/sedaci_soupravy/kazdodenni_spanni',views.kazdodenni_spanni,name="kazdodenni_spanni"),
    path('obyvaci_pokoj/obyvaci_steny',views.obyvaci_steny,name="obyvaci_steny"),
    path('obyvaci_pokoj/obyvaci_steny/komody',views.ob_komody,name="obkomody"),
    path('obyvaci_pokoj/obyvaci_steny/tv_stolky',views.tv_stolky,name="tv_stolky"),
    path('obyvaci_pokoj/konferencni_stolky',views.konferencni_stolky,name="konferencni_stolky"),
    path('obyvaci_pokoj/sakypaky',views.sakypaky,name="sakypaky"),
    path('kuchyne/kuchynske_linky',views.kuchynske_linky,name="kuchynske_linky"),
    path('kuchyne/kuchynske_linky/blokove',views.blokove,name="blokove"),
    path('kuchyne/kuchynske_linky/na_miru',views.na_miru,name="na_miru"),
    path('kuchyne/jidelni_stolky_sety',views.jidelni_stolky_sety,name="jidelni_stolky_sety"),
    path('kuchyne/jidelni_stolky_sety/jidelni_zidle',views.jidelni_zidle,name="jidelni_zidle"),
    path('detsky_pokoj/postele',views.detsky_postele,name="detsky_postele"),
    path('detsky_pokoj/postele/caloun',views.caloun,name="caloun"),
    path('detsky_pokoj/postele/poschodi',views.poschodi,name="poschodi"),
    path('detsky_pokoj/sestavy',views.sestavy,name="sestavy"),
    path('detsky_pokoj/zidle',views.detsky_zidle,name="detsky_zidle"),
    path('ostatni/kancelare',views.kancelare,name="kancelare"),
    path('ostatni/predsine',views.predsine,name="predsine"),
    path('ostatni/regaly',views.regaly,name="regaly"),
    path('ostatni/zidle',views.ostatni_zidle,name="ostatni_zidle"),

    
    


    # path('<int:listing_id>',views),
]
