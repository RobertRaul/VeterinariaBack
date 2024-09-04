from rest_framework.routers import DefaultRouter
from apps.clientes.api.views.clientes_views import ClienteViewSet

router = DefaultRouter()
router.register(r"cliente", ClienteViewSet, basename="clientes_viewset")

urlpatterns = router.urls
