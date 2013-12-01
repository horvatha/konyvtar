from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings

from konyvtar import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', views.index, name='index'),
    url(r'^konyvek/$', views.konyvek, name='konyvek'),
    url(r'^szerzok/$', views.szerzok, name='szerzok'),
    url(r'^konyv/(?P<konyv_id>\d+)$', views.konyv_reszletek, name='konyv_reszletek'),
    url(r'^szerzo/(?P<szerzo_id>\d+)$', views.szerzo_reszletek, name='szerzo_reszletek'),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
