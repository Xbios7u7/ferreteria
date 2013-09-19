from django.conf.urls import patterns, include, url
from app.views import cliente

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'app.views.home', name='home'),
    url(r'^B/$', 'app.views.Busqueda', name='Busqueda'),
    url(r'^F/$', 'app.views.Factura', name='Factura'),
    url(r'^V/(\d+)/$', 'app.views.Ventash'),
    url(r'^IP/(\d+)/$','app.views.Precio'),
    url(r'^F/(\d+)/$','app.views.GF'),
    url(r'^PRINT/F/(\d+)/$','app.views.PrintF'),
    url(r'^F/C/(\d+)/$','app.views.FI'),
    url(r'^G/(\d+)/(\d+)/$','app.views.Guardar1'),
    #url(r'^articles/(?P<year>\d{4})/$', 'news.views.year_archive'),
  
    url(r'^s/$','app.views.salir'),  
    url(r'^CAJAC/$','app.views.CCajaV'),
	url(r'^IP/$', 'app.views.Ing_Prd'),
    url(r'^IC/(\d+)/$', 'app.views.Icliente', name='Icliente'),
	#url(r'^ICL/$', 'app.views.Ic', name='Ic'),
    url(r'^IP/CBT/$', 'app.views.Cbing', name='Cbing'),
	url(r'^login/$', 'app.views.login'),
    url(r'^XLSV/(\d+)/$', 'app.views.xls_simple'),
    
    # url(r'^ferreteria/', include('ferreteria.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    url(r'^about/$', cliente.as_view(), name='about')
)
