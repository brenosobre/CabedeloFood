from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('restaurante/<int:restaurante_id>/avaliacoes/', views.avaliacoes, name='avaliacoes'),
    path('ranking/', views.ranking, name='ranking'),
    path('mapa/', views.mapa_restaurantes, name='mapa'), # Nova Rota do Ranking
]