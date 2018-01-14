from django.db import models
from django.utils import timezone


class FlatPanelDispla(models.Model):
    rozmiar_ekranu = models.CharField(max_length=200)
    producent_ekranu = models.CharField(max_length=200)
    data_testu = models.DateTimeField('date published')
    osoba_testujaca = models.CharField(max_length=200)
    numer_kartonu = models.CharField(max_length=200)
    numer_palety = models.CharField(max_length=200)