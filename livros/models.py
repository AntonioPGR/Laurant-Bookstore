from django.db import models

class Livro(models.Model):
  
  titulo = models.CharField(max_length=100, null=False, blank=False)
  autor = models.CharField(max_length=30, null=False, blank=False)
  capa = models.CharField(max_length=100, null=False, blank=False)
  sinopse = models.TextField(max_length=500, null=False, blank=False)
  preco = models.FloatField(null=False, blank=False)

  def __str__(self):
    return f"Livro [titulo={self.titulo}]"