import datetime
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from utils.permissions import IsStaffOrReadOnly, IsAdminOrReadOnly
from . import models, serializers

###################################### ACTOR API ######################################
class ActorListAPI(generics.ListCreateAPIView):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        actors = self.get_queryset()
        """
            Actor filters:
            'name': returns all the actors which name match the given string
            'last_name': returns all the actors which last_name match the given string
        """
        actors = actors if request.GET.get('name', None) is None else actors.filter(name__icontains=request.GET.get('name'))
        actors = actors if request.GET.get('last_name', None) is None else actors.filter(last_name__icontains=request.GET.get('last_name'))
        
        page = self.paginate_queryset(actors)
        response = Response()
        if page is not None:
            serializer = serializers.ActorSerializer(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(actors, many=True)
            response.data = serializer.data
        return response

class ActorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Actor.objects.all()
    serializer_class = serializers.ActorSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            actor = models.Actor.objects.get(pk=pk)
            actor.soft_delete()
            serializer = serializers.ActorSerializer(actor)
            return Response(data=serializer.data, status=httpStatus)
        except models.Actor.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)


###################################### DIRECTOR API ######################################
class DirectorListAPI(generics.ListCreateAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        directors = self.get_queryset()
        """
            Director filters:
            'name': returns all the directors which name match the given string
            'last_name': returns all the directors which last_name match the given string
        """
        directors = directors if request.GET.get('name', None) is None else directors.filter(name__icontains=request.GET.get('name'))
        directors = directors if request.GET.get('last_name', None) is None else directors.filter(last_name__icontains=request.GET.get('last_name'))
        
        page = self.paginate_queryset(directors)
        response = Response()
        if page is not None:
            serializer = serializers.DirectorSerializer(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(directors, many=True)
            response.data = serializer.data
        return response

class DirectorDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Director.objects.all()
    serializer_class = serializers.DirectorSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            director = models.Director.objects.get(pk=pk)
            director.soft_delete()
            serializer = serializers.DirectorSerializer(director)
            return Response(data=serializer.data, status=httpStatus)
        except models.Director.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)


###################################### GENRE API ######################################
class GenreListAPI(generics.ListCreateAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)

class GenreDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Genre.objects.all()
    serializer_class = serializers.GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            genre = models.Genre.objects.get(pk=pk)
            genre.soft_delete()
            serializer = serializers.GenreSerializer(genre)
            return Response(data=serializer.data, status=httpStatus)
        except models.Genre.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)


###################################### MOVIE API ######################################
class MovieListAPI(generics.ListCreateAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def get(self, request, *args, **kwargs):
        movies = self.get_queryset()
        """
            Movie filters:
            'name': returns all the movies which name match the given string
            'clasification': returns all the movies that match the given clasification
            'genre': returns all the movies which genre match with the given
            'director': returns all the movies made by the given director
        """
        movies = movies if request.GET.get('name', None) is None else movies.filter(name__icontains=request.GET.get('name'))
        movies = movies if request.GET.get('clasification', None) is None else movies.filter(clasification=request.GET.get('clasification'))
        movies = movies if request.GET.get('genre', None) is None else movies.filter(genre=request.GET.get('genre'))
        movies = movies if request.GET.get('director', None) is None else movies.filter(director=request.GET.get('director'))
        
        page = self.paginate_queryset(movies)
        response = Response()
        if page is not None:
            serializer = serializers.MovieSerializerRead(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(movies, many=True)
            response.data = serializer.data
        return response

    def create(self, request, *args, **kwargs):
        """
        {
            "name": "Avengers Endgame",
            "overview": "The revenge against Thanos",
            "duration": 158,
            "clasification": "2",
            "director": 1,
            "genre": 1
            "casting": [
                1,
                2,
                3
            ]
        }
        """
        write_serializer = serializers.MovieSerializerWrite(data=request.data)
        if write_serializer.is_valid():
            movie = write_serializer.save()
            
            read_serializer = serializers.MovieSerializerRead(movie)
            return Response(data=read_serializer.data, status=status.HTTP_201_CREATED)
        else:
            instance = None
            return Response(data=write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Movie.objects.all()
    serializer_class = serializers.MovieSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def put(self, request, pk, *args, **kwargs):
        try:
            movie = models.Movie.objects.get(pk=pk)
            edit_serializer = serializers.MovieSerializerWrite(movie, data=request.data, partial=True)
            if edit_serializer.is_valid():
                movie = edit_serializer.save()
                
                read_serializer = serializers.MovieSerializerRead(movie)
                return Response(data=read_serializer.data, status=status.HTTP_200_OK)
            else:
                instance = None
                return Response(data=edit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Movie.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)

    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            movie = models.Movie.objects.get(pk=pk)
            movie.soft_delete()
            serializer = serializers.MovieSerializer(movie)
            return Response(data=serializer.data, status=httpStatus)
        except models.Movie.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)


###################################### FORMAT API ######################################
class FormatListAPI(generics.ListCreateAPIView):
    queryset = models.Format.objects.all()
    serializer_class = serializers.FormatSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def create(self, request, *args, **kwargs):
        """
        {
            "name": "Dob 3D",
            "price": 60
        }
        """
        write_serializer = serializers.FormatSerializerWrite(data=request.data)
        if write_serializer.is_valid():
            movie_format = write_serializer.save()
            
            read_serializer = serializers.FormatSerializerRead(movie_format)
            return Response(data=read_serializer.data, status=status.HTTP_201_CREATED)
        else:
            instance = None
            return Response(data=write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FormatDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Format.objects.all()
    serializer_class = serializers.FormatSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def put(self, request, pk, *args, **kwargs):
        try:
            m_format = models.Format.objects.get(pk=pk)
            edit_serializer = serializers.FormatSerializerWrite(m_format, data=request.data, partial=True)
            if edit_serializer.is_valid():
                m_format = edit_serializer.save()
                
                read_serializer = serializers.FormatSerializerRead(m_format)
                return Response(data=read_serializer.data, status=status.HTTP_200_OK)
            else:
                instance = None
                return Response(data=edit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Format.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)
    
    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            m_format = models.Format.objects.get(pk=pk)
            m_format.soft_delete()
            serializer = serializers.FormatSerializer(m_format)
            return Response(data=serializer.data, status=httpStatus)
        except models.Format.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)


###################################### SCREENING API ######################################
class ScreeningListAPI(generics.ListCreateAPIView):
    queryset = models.Screening.objects.all()
    serializer_class = serializers.ScreeningSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def create(self, request, *args, **kwargs):
        """
        {
            "movie": 1,
            "movie_format": 1
        }
        """
        write_serializer = serializers.ScreeningSerializerWrite(data=request.data)
        if write_serializer.is_valid():
            screening = write_serializer.save()
            
            read_serializer = serializers.ScreeningSerializerRead(screening)
            return Response(data=read_serializer.data, status=status.HTTP_201_CREATED)
        else:
            instance = None
            return Response(data=write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ScreeningDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Screening.objects.all()
    serializer_class = serializers.ScreeningSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def put(self, request, pk, *args, **kwargs):
        try:
            screening = models.Screening.objects.get(pk=pk)
            edit_serializer = serializers.ScreeningSerializerWrite(screening, data=request.data, partial=True)
            if edit_serializer.is_valid():
                screening = edit_serializer.save()
                
                read_serializer = serializers.ScreeningSerializerRead(screening)
                return Response(data=read_serializer.data, status=status.HTTP_200_OK)
            else:
                instance = None
                return Response(data=edit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Screening.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)

    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            screening = models.Screening.objects.get(pk=pk)
            screening.soft_delete()
            serializer = serializers.ScreeningSerializer(screening)
            return Response(data=serializer.data, status=httpStatus)
        except models.Screening.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)