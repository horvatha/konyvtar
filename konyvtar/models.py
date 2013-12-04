#!/usr/bin/env python
# coding: utf-8

__author__ = u"Fogas László Dániel"

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import datetime


# Modellek
class Szerzo(models.Model):
    """
    Szerző
    """
    class Meta:
        ordering = ['nev']
        verbose_name = u'Szerző'
        verbose_name_plural = u'Szerzők'

    nev = models.CharField(u'Szerző neve', max_length=100)
    szuletett = models.DateTimeField(u'Született', blank=True, null=True)
    elhunyt = models.DateTimeField(u'Elhunyt', blank=True, null=True)
    nemzetiseg = models.CharField(u'Nemzetiség', max_length=50, blank=True, null=True)
    eletrajz = models.TextField(u'Életrajz', blank=True, null=True)

    def __unicode__(self):
        return self.nev

class Konyv(models.Model):
    """
    Könyv. Egy könyvnek lehet több szerzője is
    """

    class Meta:
        ordering = ['cim']
        verbose_name = u'Könyv'
        verbose_name_plural = u'Könyvek'

    cim = models.CharField(u'Cím', max_length=200)
    leiras = models.CharField(u'Leírás', max_length=500, blank=True, null=True)
    szerzo = models.ManyToManyField(Szerzo)
    isbn = models.CharField(u'ISBN', max_length=50, blank=True, null=True)
    megjelenes = models.DateField(u'Megjelenés dátuma', blank=True, null=True)
    kiado = models.CharField(u'Kiadó', max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.cim

class Kolcsonzes(models.Model):
    """
    Egy konkrét kölcsönzés. A felhasználóhoz tartozik: egy felhasználónak lehet több kölcsönzése
    is, ugyanazt a könyvet kikölcsönözheti többször is, több könyvet is kölcsönözhet egyszerre.
    """

    class Meta:
        ordering = ['-datum']
        verbose_name = u'Kölcsönzés'
        verbose_name_plural = u'Kölcsönzések'

    felhasznalo = models.ForeignKey(User)
    konyv = models.ManyToManyField(Konyv)
    datum = models.DateTimeField(u'Kölcsönzés dátuma')
    visszahozta = models.BooleanField(u'Visszahozta', default=False)

    def lejart(self):
        """
        Van-e tartozás a jelenlegi kölcsönzöshez (ha 30 napon túl nem hozta vissza a könyveket)
        """
        return self.datum <= timezone.now() - datetime.timedelta(days=30)

    # Lejárt mező logikaira állítása (admin oldali megjelenítés miatt)
    lejart.boolean = True
    lejart.short_description = u'Határidő lejárt'

    def konyvek_szama(self):
        """
        Visszaadja a kikölcsönzött könyvek számát
        """
        return self.konyv.count()

    konyvek_szama.short_description = u'Könyvek száma'

    def felhasznalo_neve(self):
        """
        Visszaadja a felhasználó teljes nevét
        """
        return " ".join([self.felhasznalo.last_name, self.felhasznalo.first_name])

    felhasznalo_neve.short_description = u'Kölcsönző neve'
