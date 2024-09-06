from django.urls import path
from apps.vet.api_views.cliente_views import LoginView
from apps.vet.api_views.patient_views import PatientViewDetail

urlpatterns = [
    # Cliente
    path("login/", LoginView.as_view(), name="login"),
    path("paciente/<int:pk>", PatientViewDetail.as_view(), name="paciente_view_detail")
]
