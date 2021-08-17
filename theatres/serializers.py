from rest_framework import serializers
from django.conf import settings
from .models import Theatre, Show, Seat
from movies.serializers import ScreeningSerializerRead

class SeatSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = (
            'id',
            'row',
            'number',
            'status',
            'theatre'
        )
        read_only_fields = ('id', 'theatre')

class SeatSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = (
            'row',
            'number',
            'status',
            'theatre'
        )
        read_only_fields = ('theatre',)

class TheatreSerializerRead(serializers.ModelSerializer):
    # seats = SeatSerializerRead(many=True)
    class Meta:
        model = Theatre 
        fields = (
            'id',
            'row_count',
            'column_count',
            'seats',
            'rest_time'
        )
        read_only_fields = ('id',)

class TheatreSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Theatre 
        fields = (
            'row_count',
            'column_count',
            'seats',
            'rest_time'
        )

class ShowSerializerRead(serializers.ModelSerializer):
    schedule = serializers.DateTimeField(format=settings.DATE_TIME_FORMAT)
    screening = ScreeningSerializerRead(many=False)
    theatre = TheatreSerializerRead(many=False)
    class Meta:
        model = Show
        fields = (
            'id',
            'schedule',
            'screening',
            'theatre'
        )
        read_only_fields = ('id', 'schedule', 'screening', 'theatre')

class ShowSerializerWrite(serializers.ModelSerializer):
    schedule = serializers.DateTimeField(format=settings.DATE_TIME_FORMAT, input_formats=[settings.DATE_TIME_FORMAT, settings.DATE_TIME_FORMAT_ALT])
    class Meta:
        model = Show
        fields = (
            'schedule',
            'screening',
            'theatre'
        )