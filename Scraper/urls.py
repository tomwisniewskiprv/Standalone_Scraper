from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.scraper, name='scraper_main_view'),
    url(r'^about$', views.about, name='scraper_about_view'),

    url(r'^options$', views.options, name='scraper_options'),
]
