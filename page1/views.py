from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import (render_to_response,
                              HttpResponseRedirect, redirect)
from django.http import HttpResponse, QueryDict
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage
from django.db.models import Q
from page1.models import *

from django.core.paginator import Paginator, EmptyPage

def home(request):
    liste_entreprise  = [entreprises.entreprise_nom for entreprises in Entreprise.objects.all()]
    liste_proprietaire  = [representants.nom_proprietaire for representants in Representant.objects.all()]
    liste_secteur  = [secteur.secteur_nom for secteur in Secteur.objects.all()]
    liste = liste_entreprise + liste_proprietaire + liste_secteur
    context= {'liste':liste}
    print liste
    return render_to_response('home.html',context)
    
def search (request):
    context = {}
    query = request.GET.get('q', '')
    secteur = Secteur.objects.all()
    if query:
        qset = (
                Q(proprietaire__code_proprietaire__icontains=query) |
                Q(proprietaire__nom_proprietaire__icontains=query) |
                Q(proprietaire__prenom_proprietaire__icontains = query) |
                Q(proprietaire__numero_proprietaire__icontains = query) |
                Q(entreprise_nom__icontains = query) |
                Q(region__nom_region__icontains = query) |
                Q(entreprise_secteur__secteur_nom__icontains = query) |
                Q(entreprise_nom__icontains = query)
            )
    resultat = Entreprise.objects.filter(qset).distinct()
    liste_cordonnee  = list()
    for cordonnee in resultat:
        #~ liste_cordonnee.append(cordonnee.entreprise_nom.encode('unicode-escape'))
        liste_cordonnee.append(cordonnee.cordonnee_longtitude)
        liste_cordonnee.append(cordonnee.cordonnee_laltitude)
    print liste_cordonnee
    i = 0
    coordonnee_filter = list()
    while i < len(liste_cordonnee):
        select_cordonne = liste_cordonnee[:2]
        coordonnee_filter.append(select_cordonne)
        del liste_cordonnee[:2]
    print coordonnee_filter
    context.update({'resultat':resultat,'coordonnee_filter':coordonnee_filter})
    
    return render_to_response('resultat.html',context)
