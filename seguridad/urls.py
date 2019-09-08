from django.conf.urls import url,re_path
from django.urls import path, include
from seguridad import views

urlpatterns = [
  url(r'^$',views.HomePageView.as_view(),name="index"),
  url(r'^busqueda/$',views.BusquedaView.as_view(),name="Buscar"),
  path('accounts/', include('django.contrib.auth.urls')),
]
