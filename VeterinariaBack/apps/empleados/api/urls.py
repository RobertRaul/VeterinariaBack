from django.urls import path
from apps.empleados.api.api import CargoApiView

urlpatterns=[
    path('cargos/',CargoApiView.as_view(),name='cargo_api')
]