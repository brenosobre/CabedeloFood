from django.db import models
from django.db.models import Avg
from django.utils import timezone

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(blank=True, null=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    imagem = models.ImageField(upload_to='fotos_restaurantes/', blank=True, null=True)
    link_cardapio = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    
    # CAMPOS DO MAPA
    latitude = models.FloatField(help_text="Ex: -6.9811", blank=True, null=True)
    longitude = models.FloatField(help_text="Ex: -34.8339", blank=True, null=True)
    
    # CAMPOS DE HORÁRIO
    hora_abertura = models.TimeField(blank=True, null=True, help_text="Ex: 18:00")
    hora_fecho = models.TimeField(blank=True, null=True, help_text="Ex: 23:30")
    
    def media_estrelas(self):
        media = self.avaliacoes.aggregate(Avg('estrelas'))['estrelas__avg']
        if media is not None:
            return round(media, 1)
        return 0
        
    def esta_aberto(self):
        if self.hora_abertura is None or self.hora_fecho is None:
            return None 
            
        agora = timezone.localtime(timezone.now()).time()
        
        if self.hora_abertura <= self.hora_fecho:
            return self.hora_abertura <= agora <= self.hora_fecho
        else:
            return agora >= self.hora_abertura or agora <= self.hora_fecho
    
    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    restaurante = models.ForeignKey(Restaurante, related_name='avaliacoes', on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    OPCOES_ESTRELAS = [(1, '1 Estrela'), (2, '2 Estrelas'), (3, '3 Estrelas'), (4, '4 Estrelas'), (5, '5 Estrelas')]
    estrelas = models.IntegerField(choices=OPCOES_ESTRELAS)
    comentario = models.TextField()
    
    # CAMPO DE MÍDIA PARA FOTOS E VÍDEOS CURTOS
    midia = models.FileField(upload_to='avaliacoes/midias/', blank=True, null=True, verbose_name="Foto ou Vídeo")
    
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.autor} - {self.estrelas} Estrelas para {self.restaurante.nome}"

class FotoRestaurante(models.Model):
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='fotos', verbose_name="Restaurante")
    imagem = models.ImageField(upload_to='restaurantes/galeria/', verbose_name="Imagem")
    legenda = models.CharField(max_length=100, blank=True, null=True, verbose_name="Legenda/Prato")

    def __str__(self):
        return f"Foto de {self.restaurante} - {self.legenda or 'Sem legenda'}"