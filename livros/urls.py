from django.urls import path
from livros.views import loja, livro

urlpatterns = [
    path('', loja),
    path('livro', livro)
]
