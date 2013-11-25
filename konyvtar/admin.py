# coding: utf-8

from django.contrib import admin
from konyvtar.models import *
from django.forms import SelectMultiple

class KolcsonzesAdmin(admin.ModelAdmin):
    # Megjelenítendő mezők
    list_display = ('felhasznalo_neve', 'felhasznalo', 'datum', 'konyvek_szama', 'visszahozta', 'lejart')

    # Könyvválasztó listbox méretének beállítása
    formfield_overrides = { models.ManyToManyField: {'widget': SelectMultiple(attrs={'size':'30'})} }

    # Szűrni lehessen
    list_filter = ['datum']


# Hozzárendelés
admin.site.register(Kolcsonzes, KolcsonzesAdmin)
admin.site.register(Konyv)
admin.site.register(Szerzo)

