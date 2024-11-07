from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Autor
from .serializers import AutorSerializer
# Create your views here.
class AutorView(APIView):

    #define as ações quando recebe um requisicao do tipo post
    def post(self, request):

        #instancia o serialize com os dados recebidos no 'request'
        serializer =AutorSerializer(data=request.data)
        if serializer.is_valid():

            #se o formato recebido estiver correto, salva os dados no banco de dados
            serializer.save()

            #retorna com o codigo 201 e os dados do serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        #se o serializer não for valido, retorna erro 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    """
    View para recuperar, atualizar ou deletar um autor específico.
    """
    def get(self, request):
        autors = Autor.objects.all()
        serializer = AutorSerializer(autors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class AutorReadUpdateDeleteView(APIView):   
    def get(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)

        '''
        try:
            autor = Autor.objects.get(pk=pk)
        except Autor.DoesNotExist:
            return Response({'detail': 'Autor não encontrado.'}, status=status.HTTP_404_NOT_FOUND)
        '''

        serializer = AutorSerializer(autor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        autor = get_object_or_404(Autor, pk=pk)
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)