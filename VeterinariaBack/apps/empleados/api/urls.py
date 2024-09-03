from django.urls import path
from apps.empleados.api.views.empleados_views import CargoApiView

urlpatterns=[
    path('cargos/',CargoApiView.as_view(),name='cargo_api')
]