import json
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Restaurante, Avaliacao, Categoria
from .forms import AvaliacaoForm

def home(request):
    # Captura os parâmetros passados na barra de endereço (URL)
    categoria_filtro = request.GET.get('categoria')
    termo_busca = request.GET.get('busca') 
    
    categorias = Categoria.objects.all()
    restaurantes = Restaurante.objects.all()

    # Filtra pelo nome se o utilizador pesquisou algo
    if termo_busca:
        restaurantes = restaurantes.filter(nome__icontains=termo_busca)

    # Filtra pela categoria se o utilizador clicou numa
    if categoria_filtro:
        restaurantes = restaurantes.filter(categoria__nome=categoria_filtro)

    return render(request, 'restaurantes/index.html', {
        'restaurantes': restaurantes,
        'categorias': categorias,
        'categoria_atual': categoria_filtro,
        'termo_busca': termo_busca 
    })

def avaliacoes(request, restaurante_id):
    restaurante = get_object_or_404(Restaurante, id=restaurante_id)
    lista_avaliacoes = restaurante.avaliacoes.all().order_by('-data_criacao')

    if request.method == 'POST':
        form = AvaliacaoForm(request.POST)
        if form.is_valid():
            nova_avaliacao = form.save(commit=False)
            nova_avaliacao.restaurante = restaurante
            nova_avaliacao.save()
            return redirect('avaliacoes', restaurante_id=restaurante.id)
    else:
        form = AvaliacaoForm()

    return render(request, 'restaurantes/avaliacoes.html', {
        'restaurante': restaurante,
        'avaliacoes': lista_avaliacoes,
        'form': form
    })

def ranking(request):
    # Calcula a média de estrelas, exclui quem não tem avaliação e ordena do maior para o menor
    restaurantes_rank = Restaurante.objects.annotate(
        media_estrelas=Avg('avaliacoes__estrelas')
    ).exclude(media_estrelas__isnull=True).order_by('-media_estrelas')
    
    return render(request, 'restaurantes/ranking.html', {'restaurantes': restaurantes_rank})

def mapa_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    # Converte os restaurantes para um formato JSON limpo para o mapa
    restaurantes_data = [
        {
            "id": r.id,
            "nome": r.nome,
            "endereco": r.endereco,
            "latitude": r.latitude,
            "longitude": r.longitude
        }
        for r in restaurantes
    ]
    return render(request, 'restaurantes/mapa.html', {
        'restaurantes_json': restaurantes_data
    })