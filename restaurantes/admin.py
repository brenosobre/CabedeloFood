from django.contrib import admin
from .models import Restaurante, Avaliacao, Categoria

admin.site.register(Categoria)
admin.site.register(Restaurante)
admin.site.register(Avaliacao)