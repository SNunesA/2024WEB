from django.db import models
# conceito ORM, models é usado para o banco de dados
# Create your models here.
# cada classe representa uma tabela no banco de dados
class Aluno(models.Model):
    # cada variavel é uma coluna
    nome=models.CharField(max_length=200)
    data_nascimento=models.DateField("date published")
    def __str__(self):
        return self.nome
class Curso(models.Model):
    nome=models.CharField(max_length=200)
    def __str__(self):
        return self.nome
class Disciplina(models.Model):
    curso=models.ForeignKey(Curso, on_delete=models.CASCADE) #chave estrangeira de curso com cascata
    nome=models.CharField(max_length=200)
    codigo=models.CharField(max_length=6,null=True)
    def __str__(self):
        # faz o nome da disciplina ser printada la no html
        return self.nome 