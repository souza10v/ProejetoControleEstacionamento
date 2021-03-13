from django.urls import path, include
from .views import (
    home,
    lista_pessoas,
    lista_veiculus,
    lista_movrotativos,
    lista_mensalistas,
    lista_movmensalistas,
    pessoa_novo)

urlpatterns = [
    path('', home, name='core_home'),
    path('pessoas', lista_pessoas, name='core_lista_pessoas'),
    path('pessoas-novo', pessoa_novo, name='core_pessoa_novo'),
    path('veiculos', lista_veiculus, name='core_lista_veiculos'),
    path('movrotativos', lista_movrotativos, name='core_lista_movrotativos'),
    path('mensalistas', lista_mensalistas, name='core_lista_mensalistas'),
    path('movmensalistas', lista_movmensalistas, name='core_lista_mensalistas')

]
