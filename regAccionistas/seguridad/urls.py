# seguridad/urls.py
#tu vieja es re weona#

from django.conf.urls import url,re_path
from django.urls import path, include
from seguridad import views


urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    path('accounts/', include('django.contrib.auth.urls'))
]