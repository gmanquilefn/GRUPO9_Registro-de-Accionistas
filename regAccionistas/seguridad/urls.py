# seguridad/urls.py
#tu vieja es re weona#

from django.conf.urls import url,re_path
from django.urls import path, include
from seguridad import views


urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'^index/',views.HomePageView.as_view(),name="index"),
    url(r'^accionista_form/',views.HomePageView2.as_view(),name="accionista_form"),
    path('accounts/', include('django.contrib.auth.urls')),
]