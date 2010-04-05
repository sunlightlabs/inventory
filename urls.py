from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^inventory/', include('inventory.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # items to admin interface
    url(r'^item/(?P<id>\d+)/$', 'QRInventory.views.item_redir', name='item_redir'),

    # index view
    url(r'^$', 'QRInventory.views.index', name='index')
)
