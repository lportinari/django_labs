from django.contrib import admin
from django.urls import path, include

from .views import index, CarroDetail, MontadoraDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='carro'),
    path('carro-detalhes/<int:pk>', CarroDetail, name='detalhes-carro'),
    path('montadora-detalhes/<int:pk>', MontadoraDetail, name='detalhes-montadora'),
]