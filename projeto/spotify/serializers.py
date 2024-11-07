from rest_framework import serializers
from .models import Artista, Album

class ArtistaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Artista
        fields='__all__'


class AlbumArtistaerializer(serializers.ModelSerializer):
    artista = ArtistaSerializer()

    class Meta:
        model = Album
        fields = ['id', 'titulo', 'ano_publicacao', 'descricao', 'artista']

    
    def create(self, validated_data):
        artista_data = validated_data.pop('artista')
        artista, created = Artista.objects.get_or_create(**artista_data)

        # Criar o album associado ao artista
        album = Album.objects.create(artista=artista, **validated_data)

        return album
