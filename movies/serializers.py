from rest_framework import serializers
from .models import Actor, Director, Genre, Movie, Casting, Format, Screening

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = (
            'id',
            'name',
            'last_name',
        )
        read_only_fields = ('id',)

class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director 
        fields = (
            'id',
            'name',
            'last_name'
        )
        read_only_fields = ('id',)

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = (
            'id',
            'name'
        )
        read_only_fields = ('id',)

class CastingSerializerRead(serializers.ModelSerializer):
    actor = ActorSerializer(many=False)
    class Meta:
        model = Casting
        fields = (
            'actor',
        )
        read_only_fields = ('id',)

class CastingSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Casting
        fields = (
            'actor',
        )

class MovieSerializerRead(serializers.ModelSerializer):
    director = DirectorSerializer(many=False)
    genre = GenreSerializer(many=False)
    casting = CastingSerializerRead(many=True, source='casting_set')

    class Meta:
        model = Movie
        fields = (
            'id',
            'name',
            'overview',
            'duration',
            'clasification',
            'genre',
            'director',
            'casting'
        )
        read_only_fields = ('id', 'genre', 'director', 'casting')

class MovieSerializerWrite(serializers.ModelSerializer):
    casting = CastingSerializerWrite(many=True)
    class Meta:
        model = Movie
        fields = (
            'name',
            'overview',
            'duration',
            'clasification',
            'director',
            'genre',
            'casting'
        )
    
    def create(self, validated_data):
        casting = validated_data.pop('casting')
        
        movie = Movie.objects.create(**validated_data)
        for actor in casting:
            Casting.objects.create(movie=movie, actor=actor['actor'])
        return movie
    
    def update(self, instance, validated_data):
        validated_casting = validated_data.pop('casting', None)
        updated_movie = super().update(instance, validated_data)
        # First we delete all the actors stored before the change
        # so we can create as much as the request has
        if(validated_casting is not None):
            actors = Casting.objects.filter(movie=instance)
            for actor in actors:
                actor.delete()
            for actor in validated_casting:
                Casting.objects.create(movie=updated_movie, actor=actor['actor'])
        return updated_movie

class FormatSerializerRead(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = (
            'id',
            'name',
            'price'
        )
        read_only_fields = ('id',)

class FormatSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Format
        fields = (
            'name',
            'price'
        )

class ScreeningSerializerRead(serializers.ModelSerializer):
    movie = MovieSerializerRead(many=False)
    movie_format = FormatSerializerRead(many=False)
    class Meta:
        model = Screening
        fields = (
            'id',
            'movie_format',
            'movie'
        )
        read_only_fields = ('id',)

class ScreeningSerializerWrite(serializers.ModelSerializer):
    class Meta:
        model = Screening
        fields = (
            'movie_format',
            'movie'
        )