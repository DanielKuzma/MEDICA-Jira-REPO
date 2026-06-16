from django import models

class pascjent(models.Model):
  imie = models.CharField(max_lenght = 100)
  nazwisko = models.CharField(max_lenght = 100)
