from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'cpf_cnpj']  # lista de campos que serão exibidos
    search_fields = ['user__username', 'cpf_cnpj']  # lista de campos que serão pesquisáveis

admin.site.register(UserProfile, UserProfileAdmin)

