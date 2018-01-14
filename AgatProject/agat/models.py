from datetime import datetime
from django.db import models
from django.utils import timezone


class Panel(models.Model):
	ROZMIAR_EKRANU = (
		('14', '14"'),
		('17', '17"'),
		('19', '19"'),
		('21', '21"'),
	)
	rozmiar_ekranu = models.CharField(max_length = 100, choices = ROZMIAR_EKRANU, blank=True)

	PRODUCENT_EKRANU = (
		('SAMSUNG', 'SAMSUNG'),
		('LG', 'LG'),
		('ASUS', 'ASUS'),
		('PHILIPS', 'PHILIPS'),
	)
	producent_ekranu = models.CharField(max_length = 100, choices = PRODUCENT_EKRANU, blank=True)
	osoba_testujaca = models.CharField(max_length=200, default='Jan Kowalski')

	data_testu = models.DateTimeField(default=datetime.now(), blank=True)
	numer_kartonu = models.IntegerField(blank=True)
	numer_palety = models.IntegerField(blank=True)