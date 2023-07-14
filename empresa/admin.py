from django.contrib import admin
from django.utils.safestring import mark_safe
from django.shortcuts import reverse
from .models import Empresa
from .models import Manutencao
from atividade.models import Item,Atividade


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')
    search_fields = ('nome', 'endereco')



class AtividadeInline(admin.StackedInline):
    model = Atividade
    extra = 0

    readonly_fields = ('view_activity',)

    def view_activity(self, obj):
        if obj.id:
            url = reverse('admin:atividade_atividade_change', args=[obj.id])
            return mark_safe(f'<a href="{url}">Ver Atividade</a>')
        return ''
    view_activity.short_description = 'Atividade'



class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ('id','empresa', 'data_manutencao', 'created_at', 'updated_at')
    list_filter = ('empresa', 'data_manutencao', 'created_at', 'updated_at')
    search_fields = ('empresa__nome', 'data_manutencao')
    date_hierarchy = 'data_manutencao'
    inlines = [AtividadeInline]

admin.site.register(Manutencao, ManutencaoAdmin)
