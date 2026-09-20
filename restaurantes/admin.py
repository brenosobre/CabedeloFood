from django.contrib import admin
from .models import Restaurante, Avaliacao, Categoria, FotoRestaurante

class FotoRestauranteInline(admin.TabularInline):
    model = FotoRestaurante
    extra = 3  # Mostra 3 espaços para adicionar fotos

class RestauranteAdmin(admin.ModelAdmin):
    inlines = [FotoRestauranteInline]

# Registos no painel de administração
admin.site.register(Categoria)
admin.site.register(Avaliacao)
admin.site.register(Restaurante, RestauranteAdmin)  # O Restaurante agora usa a classe com as fotos