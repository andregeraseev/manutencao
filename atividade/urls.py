
from django.contrib import admin
from django.urls import path
from atividade.views import adicionar_manutencao, escolher_manutencao, \
    acompanhar_manutencao_view, adicionar_atividade, editar_manutencao, excluir_atividade, detalhes_manutencao_view, \
    salvar_comentario, salvar_foto, alterar_status, item_detail, alterar_status_item, alterar_data_manutencao
from django.conf import settings
from django.conf.urls.static import static
app_name = 'atividade'

urlpatterns = [
    path('item_detail/<int:item_id>/', item_detail, name='item_detail'),
    path('alterar_status/<int:atividade_id>/', alterar_status, name='alterar_status'),
    path('salvar-comentario/<int:item_id>/', salvar_comentario, name='salvar_comentario'),
    path('salvar-foto/<int:item_id>/<str:foto_field>/', salvar_foto, name='salvar_foto'),
    # path('alterar-data-manutencao/<int:manutencao_id>/', alterar_data_manutencao, name='alterar_data_manutencao'),
    path('adicionar-manutencao/', adicionar_manutencao, name='adicionar_manutencao'),
    path('adicionar_atividade/<int:manutencao_id>/', adicionar_atividade, name='adicionar_atividade'),
    path('escolher_manutencao/', escolher_manutencao, name='escolher_manutencao'),
    path('alterar_data_manutencao/', alterar_data_manutencao, name='alterar_data_manutencao'),
    path('excluir/<int:area_id>/', excluir_atividade, name='excluir_atividade'),
    path('acompanhar-manutencao/', acompanhar_manutencao_view, name='acompanhar_manutencao'),
    path('editar_manutencao/<int:manutencao_id>/', editar_manutencao, name='editar_manutencao'),
    path('detalhes-manutencao/<int:manutencao_id>/', detalhes_manutencao_view, name='detalhes_manutencao'),
    path('alterar_status_item/<int:id>', alterar_status_item, name='alterar_status_item'),
]
