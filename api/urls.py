from django.urls import path, include
from rest_frameworks import routers

from .views import prueba, DocumentoViewSet

router = routers.DefaultRouter()
router.register(r'docs',DocumentoViewSet)


urlpatterns = [
    # path('prueba',prueba,name="prueba")
    path('',include(router.urls))
]