"""
Definition of urls for DjangoDev.
"""

from django.conf.urls import include, url
import HelloDjangoApp.views


# Django processes URL patterns in the order they appear in the array
urlpatterns = [
    url(r'^$', HelloDjangoApp.views.index, name='index'),
    url(r'^home$', HelloDjangoApp.views.index, name='home'),
    url(r'^about$', HelloDjangoApp.views.about, name='about'),
]


#===============================================
#BELOW , Default code
#===============================================
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


#urlpatterns = [
    # Examples:
    # url(r'^$', DjangoDev.views.home, name='home'),
    # url(r'^DjangoDev/', include('DjangoDev.DjangoDev.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
#]
