from django.db import connections
from django.db import models


# Create your models here.
class Eleve(models.Model):
    num= models.IntegerField(max_length=20)
    classe=models.TextField(max_length=100)
    groupe=models.TextField(max_length=100)
    nom=models.TextField(max_length=100)
    prenom=models.TextField(max_length=100)