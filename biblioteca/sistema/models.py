from django.db import models

# Create your models here.
class Autor(models.Model):
    nome=models.CharField(max_length=200)
    biografia=models.CharField(null=True,max_length=200) #biografia pode ser nula
    def __str__(self):
        return self.nome