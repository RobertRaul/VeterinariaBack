from rest_framework.routers import DefaultRouter
from apps.empleados.api.views.empleados_views import CargoViewSet

router = DefaultRouter()
router.register(r"cargos", CargoViewSet,basename='cargos_viewset')

urlpatterns = router.urls
