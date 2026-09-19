from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self):
        return self.nome

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True, blank=True)
    descricao = models.TextField(blank=True, null=True)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    imagem = models.ImageField(upload_to='fotos_restaurantes/', blank=True, null=True)
    link_cardapio = models.URLField(max_length=500, blank=True, null=True)
    instagram = models.URLField(max_length=500, blank=True, null=True)
    
    # NOVOS CAMPOS PARA O MAPA (Latitude e Longitude)
    latitude = models.FloatField(help_text="Ex: -6.9811", blank=True, null=True)
    longitude = models.FloatField(help_text="Ex: -34.8339", blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Avaliacao(models.Model):
    restaurante = models.ForeignKey(Restaurante, related_name='avaliacoes', on_delete=models.CASCADE)
    autor = models.CharField(max_length=50)
    OPCOES_ESTRELAS = [(1, '1 Estrela'), (2, '2 Estrelas'), (3, '3 Estrelas'), (4, '4 Estrelas'), (5, '5 Estrelas')]
    estrelas = models.IntegerField(choices=OPCOES_ESTRELAS)
    comentario = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.autor} - {self.estrelas} Estrelas para {self.restaurante.nome}"