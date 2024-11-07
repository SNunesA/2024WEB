from django.urls import path
from .views import ArtistaView, ArtistaReadUpdateDeleteView

urlpatterns = [
    path('artista/', ArtistaView.as_view()),
    path('artista/<int:pk>/', ArtistaReadUpdateDeleteView.as_view()),

]