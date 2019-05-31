from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.timezone import now


class Game(models.Model):
    image = models.ImageField(blank=True,null=True)
    title = models.CharField(max_length=150, verbose_name="Titel")
    authors = models.ManyToManyField("Author", related_name="games")
    publisher = models.CharField(max_length=70,verbose_name="Uitgever")
    numberofplayersminimum = models.IntegerField(verbose_name="Minimum aantal spelers")
    numberofplayersmaximum = models.IntegerField(verbose_name="Maximum aantal spelers")
    age = models.IntegerField(verbose_name="Vanaf welke leeftijd")
    duration = models.DurationField(verbose_name="Duur", help_text="Noteer het zo: [mm:ss]") 
    type = models.CharField(max_length=200)
    review = models.TextField(blank=True, null=True)
    date_reviewed = models.DateTimeField(blank=True, null=True,verbose_name="Datum review")
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
    skill = models.CharField(
        max_length=2,
        choices=SKILLS_CHOICES,
		verbose_name="Vaardigheid"
    )
    def __str__(self):
	    return self.title
		
    def list_authors(self):
        return ", ".join([author.name for author in self.authors.all()])

    def save(self, *args, **kwargs):
        if(self.review and self.date_reviewed is None):
            self.date_reviewed = now()

        super(Game, self).save(*args, **kwargs)


class Author(models.Model):
    name = models.CharField(max_length=70, verbose_name="Auteur", unique=True)

    def __str__(self):
        return self.name