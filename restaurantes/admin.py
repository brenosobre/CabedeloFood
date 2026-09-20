from django.contrib import admin
from .models import Categoria, Restaurante, Avaliacao, FotoRestaurante

class RestauranteAdmin(admin.ModelAdmin):
    # O que aparece como colunas na lista principal do painel
    list_display = ('nome', 'categoria', 'hora_abertura', 'hora_fecho')
    
    # Cria um menu lateral para filtrar facilmente
    list_filter = ('categoria',)
    
    # Adiciona uma barra de pesquisa
    search_fields = ('nome', 'endereco')

# Registar os modelos para aparecerem no Django Admin
admin.site.register(Categoria)
admin.site.register(Restaurante, RestauranteAdmin)
admin.site.register(Avaliacao)
admin.site.register(FotoRestaurante)