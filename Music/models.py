from django.db import models

class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name
    

class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    release_date = models.DateField()
    num_stars = models.DecimalField(max_digits=3, max_length=5, decimal_places=2)
    is_avilable = models.BooleanField()
    def __str__(self):
        return self.name
    