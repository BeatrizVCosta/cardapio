from django.db import models

class Cardapios (models.Model):
 nomeitem = models.CharField(max_length=100)
 preco = models.IntegerField()

def __str__(self):
 return self.nome