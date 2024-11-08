from django.db import models

# Create your models here.
# class Aluno(models.Model):
#     nome=models.CharField(max_length=200)
#     data_nascimento=models.DateTimeField("date published")

    
class Professor(models.Model):
    nome=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome=models.CharField(max_length=200)
    # sigla=models.CharField(max_length=12) DANDO ERRO
    def __str__(self):
        return self.nome

class Disciplina(models.Model):
    #chave estrangeira para Curso.
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, null=True)
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=6, null=True)

class ConteudoProgramatico(models.Model):
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name='conteudos_programaticos')
    descricao = models.TextField(null=True)


# class Disciplina(models.Model):
#     curso=models.ForeignKey(Curso, on_delete=models.CASCADE)
#     nome=models.CharField(max_length=200)
#     codigo=models.CharField(max_length=6, null=True)
    
#     alunos=models.ManyToManyField(Aluno) #relacionamento muitos pra muitos
    
# class Matricula (models.Model):
#     aluno=models.ForeignKey(Aluno,on_delete=models.CASCADE)
#     Disciplina=models.ForeignKey(Disciplina,on_delete=models.CASCADE)
#     periodo=models.IntegerField(null=True)
