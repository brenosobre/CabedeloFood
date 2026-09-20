from django.contrib import admin
from .models import Categoria, Restaurante, Avaliacao, FotoRestaurante

# Cria a secção de galeria de fotos para aparecer dentro do restaurante
class FotoRestauranteInline(admin.TabularInline):
    model = FotoRestaurante
    extra = 1  # Mostra um espaço vazio por defeito para adicionar nova foto

class RestauranteAdmin(admin.ModelAdmin):
    # O que aparece como colunas na lista principal
    list_display = ('nome', 'categoria', 'hora_abertura', 'hora_fecho')
    
    # Cria um menu lateral para filtrar
    list_filter = ('categoria',)
    
    # Adiciona a barra de pesquisa
    search_fields = ('nome', 'endereco')
    
    # Injeta a secção de fotografias no fundo da página de edição
    inlines = [FotoRestauranteInline]

# Regista os modelos no painel
admin.site.register(Categoria)
admin.site.register(Restaurante, RestauranteAdmin)
admin.site.register(Avaliacao)