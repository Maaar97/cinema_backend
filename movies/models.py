from django.db import models
from utils.models import BaseModel
from django.utils.translation import ugettext_lazy as _

class Actor(BaseModel):

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = _("actor")
        verbose_name_plural = _("actors")
        ordering = ['id',]

    def __str__(self):
        return self.name + ' ' + self.last_name

class Director(BaseModel):

    name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name = _("director")
        verbose_name_plural = _("directors")
        ordering = ['id',]

    def __str__(self):
        return self.name + ' ' + self.last_name

class Genre(BaseModel):

    name = models.CharField(max_length=25)

    class Meta:
        verbose_name = _("genre")
        verbose_name_plural = _("genres")
        ordering = ['id',]

    def __str__(self):
        return self.name

class Movie(BaseModel):
    CLASIFICATIONS = (
        ('1', 'A - Todo público'),
        ('2', 'B - Todo público, mayores de 6 años'),
        ('3', 'B12 - Mayores de 12 años'),
        ('4', 'B15 - Mayores de 15 años'),
        ('5', 'C - Mayores de 18 años')
    )

    name = models.CharField(max_length=100)
    overview = models.TextField()
    duration = models.PositiveSmallIntegerField()
    clasification = models.CharField(max_length=3, choices=CLASIFICATIONS, default='1')
    director = models.ForeignKey("movies.Director", on_delete=models.CASCADE)
    genre = models.ForeignKey("movies.Genre", on_delete=models.CASCADE)


    class Meta:
        verbose_name = _("movie")
        verbose_name_plural = _("movies")
        ordering = ['name', 'id']

    def __str__(self):
        return self.name + f' duration: {self.duration} min'

class Casting(BaseModel):

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    actor = models.ForeignKey("movies.Actor", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("casting")
        verbose_name_plural = _("castings")
        ordering = ['movie', 'id']

    def __str__(self):
        return self.id

class Format(BaseModel):

    name = models.CharField(max_length=10)
    price = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = _("format")
        verbose_name_plural = _("formats")
        ordering = ['id',]

    def __str__(self):
        return self.name

class Screening(BaseModel):

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)
    movie_format = models.ForeignKey("movies.Format", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("screening")
        verbose_name_plural = _("screenings")
        ordering = ['movie_format', 'id',]

    def __str__(self):
        return self.id

