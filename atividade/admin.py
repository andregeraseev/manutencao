
from django.contrib import admin
from .models import Atividade, Item, ItemChoise, AreaChoise

@admin.register(Atividade)
class AtividadeAdmin(admin.ModelAdmin):
    list_display = ('id', 'area', 'status')
    list_filter = ('status',)
    search_fields = ('area', 'empresa__nome')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'atividade')
    list_filter = ('atividade__area',)
    search_fields = ('descricao', 'atividade__area')

@admin.register(ItemChoise)
class ItemChoiseAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(AreaChoise)
class AreaChoiseAdmin(admin.ModelAdmin):
    list_display = ('nome',)

