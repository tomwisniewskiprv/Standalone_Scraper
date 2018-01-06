from django.conf.urls import include, url
from Scraper.views import scraper, about, options

urlpatterns = [
    url(r'^$', scraper, name='scraper'),
    url(r'^about$', about, name='about'),
    url(r'^options$', options, name='options'),
]
