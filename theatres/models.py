from django.db import models
from utils.models import BaseModel
from django.utils.translation import ugettext_lazy as _


class Seat(BaseModel):
    SEAT_STATUSES=(
        ('1', 'Libre'),
        ('2', 'Reservado'),
        ('3', 'Vendido'),
        ('4', 'Fuera de Servicio')
    )

    row = models.CharField(max_length=1)
    number = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=1, choices=SEAT_STATUSES, default='1')
    theatre = models.ForeignKey("theatres.Theatre", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("seat")
        verbose_name_plural = _("seats")
        ordering = ['theatre', 'row',]

    def __str__(self):
        return f'{self.row} {self.number}: {self.status.name}'


class Theatre(BaseModel):

    row_count = models.PositiveSmallIntegerField()
    column_count = models.PositiveSmallIntegerField()
    seats = models.PositiveSmallIntegerField()
    rest_time = models.PositiveSmallIntegerField()

    class Meta:
        verbose_name = _("theatre")
        verbose_name_plural = _("theatres")
        ordering = ['id',]

    def __str__(self):
        return self.name

    def create_theatre_seats(self):
        rows = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
        for i in range(self.row_count):
            for j in range(self.column_count):
                Seat.objects.create(
                    row = rows[i],
                    number = j+1,
                    status = '1',
                    theatre = self
                )


class Show(BaseModel):

    schedule = models.DateTimeField(auto_now=False, auto_now_add=False)
    screening = models.ForeignKey("movies.Screening", on_delete=models.CASCADE)
    theatre = models.ForeignKey("theatres.Theatre", on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("show")
        verbose_name_plural = _("shows")
        ordering = ['theatre', 'screening', 'schedule']

    def __str__(self):
        return f'{self.proyection.movie.name}: {self.schedule} - {self.theatre.id}'
