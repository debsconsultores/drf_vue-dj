from django.urls import path, include
from .views import prueba

urlpatterns = [
    path('prueba',prueba,name="prueba")
]