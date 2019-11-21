from django.conf.urls import url,re_path
from django.urls import path, include
from seguridad import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  url(r'^traspasos/$',views.HomePageView.as_view(),name="traspaso"),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)