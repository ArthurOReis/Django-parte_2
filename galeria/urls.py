from django.urls import path
from galeria.views import * #De views, em galeria, importar todos os métodos

urlpatterns = [
    path('', index, name="index"),
    path('imagem/', imagem, name="imagem"),
]