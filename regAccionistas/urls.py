from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('admin/', admin.site.urls),
  path(r'', include('seguridad.urls')),
  path(r'', include('accionista.urls')),
  path(r'', include('tercero.urls')),
  path(r'', include('traspaso.urls')),
  path(r'', include('dividendo.urls')),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)