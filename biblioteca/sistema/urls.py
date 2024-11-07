from django.urls import path
from .views import AutorView, AutorReadUpdateDeleteView

urlpatterns = [
    path('autor/', AutorView.as_view()),
    path('autor/<int:pk>/', AutorReadUpdateDeleteView.as_view()),

]