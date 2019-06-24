from django.conf.urls import url,re_path
from django.urls import path, include
from accionista import views


urlpatterns = [
    url(r'^accionista_form/',views.HomePageView.as_view(),name="accionista_form"),
    path('accounts/', include('django.contrib.auth.urls'))
]