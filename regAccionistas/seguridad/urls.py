# seguridad/urls.py


from django.conf.urls import url,re_path
from django.urls import path, include
from seguridad import views


urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'^index/',views.HomePageView.as_view(),name="index"),
    url(r'^accionista_form/',views.HomePageView2.as_view(),name="accionista_form"),
    url(r'^creacion_acc/',views.HomePageView3.as_view(),name="creacion_acc"),
    path('accounts/', include('django.contrib.auth.urls')),
]