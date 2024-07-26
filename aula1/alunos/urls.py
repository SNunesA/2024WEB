
from django.urls import path
# url ta diretamente ligado na view, o que vai ter em cada endereço url
from . import views
urlpatterns = [
    path("", views.index,name="index"),
]
