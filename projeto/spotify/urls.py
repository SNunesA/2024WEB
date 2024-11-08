from django.urls import path
from .views import ArtistaView, ArtistaReadUpdateDeleteView, AlbumAutorAPIView

urlpatterns = [
    path('artista/', ArtistaView.as_view()),
    path('artista/<int:pk>/', ArtistaReadUpdateDeleteView.as_view()),
    path('album/artista/', AlbumAutorAPIView.as_view()),

]