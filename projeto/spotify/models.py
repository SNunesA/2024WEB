from django.db import models

# Create your models here.
class Artista(models.Model):
    nome=models.CharField(max_length=200)
    genero=models.CharField(null=True,max_length=200) #biografia pode ser nula
    def __str__(self):
        return self.nome
    
class Album(models.Model):
    titulo = models.CharField(max_length=255, unique=True)
    ano_publicacao = models.IntegerField()
    descricao = models.TextField(blank=True, null=True)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo