from django.shortcuts import render
from django.http import HttpResponse
# o que vai aparecer
# Create your views here.
def index (request):
    return HttpResponse("Index pagina aluno")