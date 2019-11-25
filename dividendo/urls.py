from django.conf.urls import url,re_path
from django.urls import path, include
from dividendo import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns= [
    url(r'^dividendos/$',views.AccionesView.as_view(),name="dividendos"),
    url(r'^dividendos/pago/$',views.AccionistasView.as_view(),name="dividendos"),
    url(r'^dividendos/crear/$',views.CreateAcciones.as_view(success_url="/dividendos/"),name="crear"),

]