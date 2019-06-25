from django.conf.urls import url,re_path
from django.urls import path, include
from accionista import views

urlpatterns = [
    url(r'^accionistas/',views.HomePageView2.as_view(),name="accionistas"),
    path('accounts/', include('django.contrib.auth.urls'))
]