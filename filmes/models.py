from django.db import models
from django.core.validators import FileExtensionValidator

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    direcao = models.CharField(max_length=100)
    distribuicao = models.CharField(max_length=100, blank=True)
    capa = models.ImageField(upload_to='capas/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return f"{self.titulo} {self.direcao}"
    
class Genero(models.Model):
    nome = models.CharField(max_length=100)
    filmes = models.ManyToManyField(Filme)

    def __str__(self):
        return self.nome