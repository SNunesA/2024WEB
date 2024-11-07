# from django.urls import path
# from . import views
# urlpatterns = [
#     path("",views.index, name="index")
# ]


from django.urls import path
from .views import ProfessorView, ProfessorReadUpdateDeleteView, CursoListCreateAPIView, DisciplinaListCreateAPIView, DisciplinaRetrieveUpdateDestroyAPIView, DisciplinaConteudoCreateView


urlpatterns = [
    path('professor/', ProfessorView.as_view()),
    path('professor/<int:pk>/', ProfessorReadUpdateDeleteView.as_view(), name='professor-detail'),

     path('curso/', CursoListCreateAPIView.as_view()),
    
    path('disciplina/', DisciplinaListCreateAPIView.as_view()),
    path('disciplina/<int:pk>/', DisciplinaRetrieveUpdateDestroyAPIView.as_view()),

    path('disciplina/conteudo/', DisciplinaConteudoCreateView.as_view()),
]