# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import RequestContext, loader

from konyvtar.models import *

def index(request):
    """
    Kezdőoldal ("index.html")
    """
    context = RequestContext(request, {"konyvekszama": Konyv.objects.count(), "szerzokszama": Szerzo.objects.count()})
    template = loader.get_template("index.html")
    return HttpResponse(template.render(context))

def konyvek(request):
    """
    Könyvek listája
    """
    kl = Konyv.objects.all()
    konyvlista = kl.extra(order_by = ['cim'])
    context = RequestContext(request, {"konyvlista": konyvlista})
    template = loader.get_template("konyvek.html")
    return HttpResponse(template.render(context))

def szerzok(request):
    """
    Szerzők listája
    """
    szerzolista = Szerzo.objects.all()
    szerzolista = szerzolista.extra(order_by = ['nev'])
    context = RequestContext(request, {"szerzolista": szerzolista})
    template = loader.get_template("szerzok.html")
    return HttpResponse(template.render(context))

def konyv_reszletek(request, konyv_id):
    try:
        konyv = Konyv.objects.get(pk=konyv_id)
        context = RequestContext(request, {"konyv": konyv})
        template = loader.get_template("konyv_reszletek.html")
        return HttpResponse(template.render(context))
    except Konyv.DoesNotExist:
        raise Http404

def szerzo_reszletek(request, szerzo_id):
    try:
        szerzo = Szerzo.objects.get(pk=szerzo_id)
        context = RequestContext(request, {"szerzo": szerzo})
        template = loader.get_template("szerzo_reszletek.html")
        return HttpResponse(template.render(context))
    except Szerzo.DoesNotExist:
        raise Http404
