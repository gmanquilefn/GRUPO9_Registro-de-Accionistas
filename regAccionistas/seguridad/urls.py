# seguridad/urls.py
from django.conf.urls import url,re_path
from django.urls import path, include
from seguridad import views

urlpatterns = [
    url(r'^$',views.HomePageView.as_view(),name="index"),
    url(r'^accionistas/',views.AccionistasView.as_view(),name="accionistas"),
    url(r'^crear/',views.CreateAccionista.as_view(success_url="/accionistas/"),name="crear"),
    path('accionistas/<int:pk>/editar',views.UpdateAccionista.as_view(success_url='/accionistas/'),name='editar'),
    path('accionistas/<int:pk>/',views.DetalleAccionistaView.as_view(),name="detalle"),
    path('accounts/', include('django.contrib.auth.urls')),
]