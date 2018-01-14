from datetime import datetime
from django.db import models
from django.utils import timezone

class Panel(models.Model):
	ROZMIAR_EKRANU = (
		('wybierz', 'wybierz'),
		('14', '14"'),
		('17', '17"'),
		('19', '19"'),
		('21', '21"'),
	)
	rozmiar_ekranu = models.CharField(max_length = 100, choices = ROZMIAR_EKRANU, default='wybierz')

	PRODUCENT_EKRANU = (
		('wybierz', 'wybierz'),
		('SAMSUNG', 'SAMSUNG'),
		('LG', 'LG'),
		('ASUS', 'ASUS'),
		('PHILIPS', 'PHILIPS'),
	)
	producent_ekranu = models.CharField(max_length = 100, choices = PRODUCENT_EKRANU, default='wybierz')
	osoba_testujaca = models.CharField(max_length=200, default='Jank Kowalski')

	pub_date = models.DateTimeField('Data testu')
	numer_kartonu = models.IntegerField(default='0')
	numer_palety = models.IntegerField(default='0')