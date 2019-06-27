from django.conf.urls import url,re_path
from django.urls import path, include
from accionista import views

urlpatterns = [
  url(r'^accionistas/$',views.AccionistasView.as_view(),name="accionistas"),
  url(r'^crear/',views.CreateAccionista.as_view(success_url="/accionistas/"),name="crear"),
  re_path(r'^accionistas/(?P<pk>\d+)/editar/$',views.UpdateAccionista.as_view(success_url="/accionistas/"),name='editar'),
  re_path(r'accionistas/(?P<pk>\d+)/$',views.DetalleAccionistaView.as_view(),name="accionista"),
]