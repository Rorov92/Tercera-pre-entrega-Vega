from django.db import models

class Juegos(models.Model):
    titulo = models.CharField(max_length=256)
    nombre_autor = models.CharField(max_length=256)
    apellido_autor = models.CharField(max_length=256)
    ISBN = models.IntegerField()
        
    def __str__(self):
        return f"{self.titulo}, {self.ISBN}"

class Hardware(models.Model):
    titulo = models.CharField(max_length=256)
    nombre_autor = models.CharField(max_length=256)
    genero = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.titulo}, {self.genero}"