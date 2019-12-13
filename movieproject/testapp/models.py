from django.db import models


# Create your models here.
class moviemodel(models.Model):
    rdate=models.IntegerField()
    moviename=models.CharField(max_length=20)
    heroname=models.CharField(max_length=20)
    heroinname=models.CharField(max_length=20)
    rating=models.IntegerField()
class dummimodel(models.Model):
    rdate=models.IntegerField()
    moviename=models.CharField(max_length=20)
    heroname=models.CharField(max_length=20)
    heroinname=models.CharField(max_length=20)
    rating=models.IntegerField()
