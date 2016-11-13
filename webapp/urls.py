from django.conf.urls import url

from webapp import views

urlpatterns = [
    url(r'^$', views.findbike, name = "findbike"),
    url(r'^directions/$', views.directions, name='directions'),
    url(r'^stations/$', views.stations, name='stations'),
]
