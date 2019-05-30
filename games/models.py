from django.conf import settings
from django.db import models
from django.utils import timezone


class Game(models.Model):
   title = models.CharField(max_length=150)
   author = models.CharField(max_length=70)
   publisher = models.CharField(max_length=70)
   numberofplayersminimum = models.IntegerField()
   numberofplayersmaximum = models.IntegerField()
   age = models.IntegerField()
   duration = models.DurationField() 
   type = models.CharField(max_length=200)
   review = models.TextField(blank=True, null=True)
   date_reviewed = models.DateTimeField(blank=True, null=True)
  # score = 
   CONCENTRATIE = 'CR'
   GEDULD = 'GD'
   GEHEUGEN = 'GH'
   HOOFDREKENEN = 'HR'
   DURF = 'DR'
   HERKENNING = 'HK'
   REACTIEVERMOGEN = 'RV'
   SKILLS_CHOICES = (
       (CONCENTRATIE, 'Concentratie'),
       (GEDULD, 'Geduld'),
       (GEHEUGEN, 'Geheugen'),
       (HOOFDREKENEN, 'Hoofdrekenen'),
       (DURF, 'Durf'),
       (HERKENNING, 'Herkenning'),
       (REACTIEVERMOGEN, 'Reactievermogen'),
    )
   skills = models.CharField(
       max_length=2,
       choices=SKILLS_CHOICES,
    )