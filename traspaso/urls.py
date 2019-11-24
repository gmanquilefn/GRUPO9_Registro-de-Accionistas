from django.conf.urls import url,re_path
from django.urls import path, include
from traspaso import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^acciones/$',views.AccionesView.as_view(),name="acciones"),
    url(r'^acciones/traspaso/$',views.AccionistasView.as_view(),name="acciones"),
    url(r'^acciones/crear/$',views.CreateAcciones.as_view(success_url="/acciones/"),name="crear"),
    url(r'^acciones/(?P<pk>\d+)/editar/$',views.AccionesView2.as_view(),name='editar'),
    re_path(r'^acciones/(?P<pk>\d+)/editar2/$',views.UpdateAcciones.as_view(success_url="/acciones/"),name='editar'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
