from django.conf.urls import url,re_path
from django.urls import path, include
from tercero import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^terceros/$',views.TercerosView.as_view(),name="terceros"),
  url(r'^crear/',views.CreateTercero.as_view(success_url="/terceros/"),name="crear"),
  re_path(r'^terceros/(?P<pk>\d+)/editar/$',views.UpdateTercero.as_view(success_url="/terceros/"),name='editar'),
  re_path(r'terceros/(?P<pk>\d+)/$',views.DetalleTerceroView.as_view(),name="tercero"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)