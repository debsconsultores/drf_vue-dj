from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import prueba, DocumentoViewSet, \
    CategoriaViewSet, SubCategoriaViewSet, \
    ProductoViewSet, ProveedorViewSet, \
    ComprasViewSet, ComprasDetViewSet, \
    ClienteViewSet, FacturasDetViewSet, \
    FacturasViewSet

router = routers.DefaultRouter()
router.register(r'docs',DocumentoViewSet)
router.register(r'categoria',CategoriaViewSet)
router.register(r'subcategoria',SubCategoriaViewSet)
router.register(r'producto',ProductoViewSet)
router.register(r'proveedor',ProveedorViewSet)
router.register(r'compras', ComprasViewSet)
router.register(r'compras-detalle', ComprasDetViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'facturas', FacturasViewSet)
router.register(r'facturas-detalle', FacturasDetViewSet)

urlpatterns = [
    # path('prueba',prueba,name="prueba")
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
