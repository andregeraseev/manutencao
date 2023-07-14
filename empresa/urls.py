
from django.contrib import admin
from django.urls import path
from empresa.views import cadastro_empresa, editar_empresa, listar_empresas
from django.conf import settings
from django.conf.urls.static import static
app_name = 'empresa'

urlpatterns = [

    path('cadastro_empresa/', cadastro_empresa, name='cadastro_empresa'),
    path('editar_empresa/<int:empresa_id>/', editar_empresa, name='editar_empresa'),
    path('listar_empresas/', listar_empresas, name='listar_empresas'),

]
