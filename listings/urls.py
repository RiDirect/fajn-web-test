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
    path('container',views.container,name="container"),
    path('postele',views.category_listings,name="postele"),
    path('postele/<slug:slug>',views.postele_details,name="postele_details"),
    path('loznice/postele/calounene_postele',views.calounene_postele,name="calounene_postele"),
    path('loznice/postele/calounene_postele/<slug:slug>',views.calounene_postele_details,name="calounene_postele_details"),
    path('loznice/postele/postele_z_masivu',views.postele_z_masivu,name="postele_z_masivu"),
    path('loznice/postele/postele_z_masivu/<slug:slug>',views.postele_z_masivu_details,name="postele_z_masivu_details"),
    path('loznice/postele/postelove_ramy',views.postelove_ramy,name="postelove_ramy"),
    path('loznice/postele/postelove_ramy/<slug:slug>',views.postelove_ramy_details,name="postelove_ramy_details"),
    path('loznice/valendy',views.valendy,name="valendy"),
    path('loznice/valendy/<slug:slug>',views.valendy_details,name="valendy_details"),
    path('loznice/komody',views.komody,name="komody"),
    path('loznice/komody/<slug:slug>',views.komody_details,name="komody_details"),
    path('loznice/skrine',views.skrine,name="skrine"),
    path('loznice/skrine/<slug:slug>',views.skrine_details,name="skrine_details"),
    path('loznice/nocni_stolky',views.nocní_stolky,name="nocni_stolky"),
    path('loznice/nocni_stolky/<slug:slug>',views.nocni_stolky_details,name="nocní_stolky_details"),
    path('loznice/matrace',views.matrace,name="matrace"),
    path('loznice/matrace/<slug:slug>',views.matrace_details,name="matrace_details"),
    path('obyvaci_pokoj/sedaci_soupravy',views.sedaci_soupravy,name="sedaci_soupravy"),
    path('obyvaci_pokoj/sedaci_soupravy/<slug:slug>',views.sedaci_soupravy_details,name="sedaci_soupravy_details"),
    path('obyvaci_pokoj/sedaci_soupravy/rohove',views.rohove,name="rohove"),
    path('obyvaci_pokoj/sedaci_soupravy/rohove/<slug:slug>',views.rohove_details,name="rohove_details"),
    path('obyvaci_pokoj/sedaci_soupravy/levne_sedaci_soupravy',views.levne_sedaci_soupravy,name="levne_sedaci_soupravy"),
    path('obyvaci_pokoj/sedaci_soupravy/levne_sedaci_soupravy/<slug:slug>',views.levne_sedaci_soupravy_details,name="levne_sedaci_soupravy_details"),
    path('obyvaci_pokoj/sedaci_soupravy/kazdodenni_spanni',views.kazdodenni_spanni,name="kazdodenni_spanni"),
    path('obyvaci_pokoj/sedaci_soupravy/kazdodenni_spanni/<slug:slug>',views.kazdodenni_spanni_details,name="kazdodenni_spanni_details"),
    path('obyvaci_pokoj/obyvaci_steny',views.obyvaci_steny,name="obyvaci_steny"),
    path('obyvaci_pokoj/obyvaci_steny/<slug:slug>',views.obyvaci_steny_details,name="obyvaci_steny_details"),
    path('obyvaci_pokoj/obyvaci_steny/komody',views.ob_komody,name="obkomody"),
    path('obyvaci_pokoj/obyvaci_steny/komody/<slug:slug>',views.ob_komody_details,name="ob_komody_details"),
    path('obyvaci_pokoj/obyvaci_steny/tv_stolky',views.tv_stolky,name="tv_stolky"),
    path('obyvaci_pokoj/obyvaci_steny/tv_stolky/<slug:slug>',views.tv_stolky_details,name="tv_stolky_details"),
    path('obyvaci_pokoj/konferencni_stolky',views.konferencni_stolky,name="konferencni_stolky"),
    path('obyvaci_pokoj/konferencni_stolky/<slug:slug>',views.konferencni_stolky_details,name="konferencni_stolky_details"),
    path('obyvaci_pokoj/sakypaky',views.sakypaky,name="sakypaky"),
    path('obyvaci_pokoj/sakypaky/<slug:slug>',views.sakypaky_details,name="sakypaky_details"),
    path('kuchyne/kuchynske_linky',views.kuchynske_linky,name="kuchynske_linky"),
    path('kuchyne/kuchynske_linky/<slug:slug>',views.kuchynske_linky_details,name="kuchynske_linky_details"),
    path('kuchyne/kuchynske_linky/blokove',views.blokove,name="blokove"),
    path('kuchyne/kuchynske_linky/blokove/<slug:slug>',views.blokove_details,name="blokove_details"),
    path('kuchyne/kuchynske_linky/na_miru',views.na_miru,name="na_miru"),
    path('kuchyne/kuchynske_linky/na_miru/<slug:slug>',views.na_miru_details,name="na_miru_details"),
    path('kuchyne/jidelni_stolky_sety',views.jidelni_stolky_sety,name="jidelni_stolky_sety"),
    path('kuchyne/jidelni_stolky_sety/<slug:slug>',views.jidelni_stolky_sety_details,name="jidelni_stolky_sety_details"),
    path('kuchyne/jidelni_stolky_sety/jidelni_zidle',views.jidelni_zidle,name="jidelni_zidle"),
    path('kuchyne/jidelni_stolky_sety/jidelni_zidle/<slug:slug>',views.jidelni_zidle_details,name="jidelni_zidle_details"),
    path('detsky_pokoj/postele',views.detsky_postele,name="detsky_postele"),
    path('detsky_pokoj/postele/<slug:slug>',views.detsky_postele_details,name="detsky_postele_details"),
    path('detsky_pokoj/postele/caloun',views.caloun,name="caloun"),
    path('detsky_pokoj/postele/caloun/<slug:slug>',views.caloun_details,name="caloun_details"),
    path('detsky_pokoj/postele/poschodi',views.poschodi,name="poschodi"),
    path('detsky_pokoj/postele/poschodi/<slug:slug>',views.poschodi_details,name="poschodi_details"),
    path('detsky_pokoj/sestavy',views.sestavy,name="sestavy"),
    path('detsky_pokoj/sestavy/<slug:slug>',views.sestavy_details,name="sestavy_details"),
    path('detsky_pokoj/zidle',views.detsky_zidle,name="detsky_zidle"),
    path('detsky_pokoj/zidle/<slug:slug>',views.detsky_zidle_details,name="detsky_zidle_details"),
    path('ostatni/kancelare',views.kancelare,name="kancelare"),
    path('ostatni/kancelare/<slug:slug>',views.kancelare_details,name="kancelare_details"),
    path('ostatni/predsine',views.predsine,name="predsine"),
    path('ostatni/predsine/<slug:slug>',views.predsine_details,name="predsine_details"),
    path('ostatni/regaly',views.regaly,name="regaly"),
    path('ostatni/regaly/<slug:slug>',views.regaly_details,name="regaly_details"),
    path('ostatni/zidle',views.ostatni_zidle,name="ostatni_zidle"),
    path("dev-kancelare",views.dev_kancelare,name="dev_kancelare"),
    path("dev-kuchyne",views.dev_kuchyne,name="dev_kuchyne"),
    path("dev-nabytek",views.dev_nabytek,name="dev_nabytek"),
    path("dev-spotrebice",views.dev_spotrebice,name="dev_spotrebice"),
    path("developerske-projekty",views.developerske_projekty,name="developerske_projekty"),

    
    


    # path('<int:listing_id>',views),
]
