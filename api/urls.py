from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .views import prueba, DocumentoViewSet

router = routers.DefaultRouter()
router.register(r'docs',DocumentoViewSet)


urlpatterns = [
    # path('prueba',prueba,name="prueba")
    path('',include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]