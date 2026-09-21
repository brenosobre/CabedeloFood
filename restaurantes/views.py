import json
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Avg
from .models import Restaurante, Avaliacao, Categoria
from .forms import AvaliacaoForm

def home(request):
    categoria_filtro = request.GET.get('categoria')
    termo_busca = request.GET.get('busca') 
    
    categorias = Categoria.objects.all()
    restaurantes = Restaurante.objects.all()

    if termo_busca:
        restaurantes = restaurantes.filter(nome__icontains=termo_busca)

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
        # request.FILES obrigatório para aceitar fotos e vídeos
        form = AvaliacaoForm(request.POST, request.FILES)
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
    restaurantes_rank = Restaurante.objects.annotate(
        media_estrelas=Avg('avaliacoes__estrelas')
    ).exclude(media_estrelas__isnull=True).order_by('-media_estrelas')
    
    return render(request, 'restaurantes/ranking.html', {'restaurantes': restaurantes_rank})

def mapa_restaurantes(request):
    restaurantes = Restaurante.objects.all()
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