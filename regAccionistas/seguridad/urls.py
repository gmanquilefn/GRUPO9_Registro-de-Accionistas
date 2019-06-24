# seguridad/urls.py

from django.conf.urls import url,re_path
from django.urls import path, include
from seguridad import views


urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'^accionista/create/$', views.AccionistaCreate.as_view(success_url='/accionista/'), name='accionista_create'),
    url(r'accionista/(?P<pk>\d+)/update/$', views.AccionistaUpdate.as_view(success_url='/accionista/'), name='accionista_update'),
    #url(r'^$',views.HomeAccionistaView.as_view(),name="vistaaccionista"),
    #path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]