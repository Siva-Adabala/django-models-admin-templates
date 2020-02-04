from django.db import models

class Runner(models.Model):
    id = models.AutoField(primary_key=True)
    MedalType = models.TextChoices('Medal', 'GOLD SILVER BRONZE NOMEDALS BETTERLUCK')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices = MedalType.choices, max_length=10, default="SILVER")

class Fruit(models.Model):
    name = models.CharField("fruit's name",max_length=100, primary_key=True)

