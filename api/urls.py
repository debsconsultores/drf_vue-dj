from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import prueba, DocumentoViewSet, \
    CategoriaViewSet, SubCategoriaViewSet, \
    ProductoViewSet

router = routers.DefaultRouter()
router.register(r'docs',DocumentoViewSet)
router.register(r'categoria',CategoriaViewSet)
router.register(r'subcategoria',SubCategoriaViewSet)
router.register(r'producto',ProductoViewSet)


urlpatterns = [
    # path('prueba',prueba,name="prueba")
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]