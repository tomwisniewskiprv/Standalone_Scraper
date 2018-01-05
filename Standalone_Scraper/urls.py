from django.conf.urls import include, url
from django.contrib import admin
from Scraper.views import scraper, about, options

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', scraper, name='scraper'),
    url(r'^options', options, name='options'),
    url(r'^about$', about, name='about'),
]
