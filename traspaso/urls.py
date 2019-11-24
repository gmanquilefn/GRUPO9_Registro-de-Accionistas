from django.conf.urls import url,re_path
from django.urls import path, include
from traspaso import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^acciones/crear/$',views.CreateAcciones.as_view(success_url="/acciones/"),name="crear"),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
