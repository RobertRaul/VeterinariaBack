from django.urls import path
from apps.empleados.api.api import CargoApiView

urlpatterns=[
    path('cargo/',CargoApiView.as_view(),name='cargo_api')
]