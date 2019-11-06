from django.urls import path, include
from .views import listar_imagens

urlpatterns = [
   path('listar_imagens/', listar_imagens, name='listar_imagens'),
]