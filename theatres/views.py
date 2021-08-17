import datetime
from rest_framework.response import Response
from rest_framework import status, generics, permissions

from utils.permissions import IsStaffOrReadOnly, IsAdminOrReadOnly
from . import models, serializers

###################################### SEAT API ######################################
class SeatListAPI(generics.ListAPIView):
    queryset = models.Seat.objects.all()
    serializer_class = serializers.SeatSerializerRead
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        seats = self.get_queryset()
        """
            Seat filters:
            'theatre': returns all the seats that belong to given theatre
        """
        seats = seats if request.GET.get('theatre', None) is None else seats.filter(name__icontains=request.GET.get('theatre'))
        
        page = self.paginate_queryset(seats)
        response = Response()
        if page is not None:
            serializer = serializers.SeatSerializerRead(page, many=True)
            response = self.paginator.get_paginated_response(serializer.data)
        else:
            serializer = self.get_serializer(seats, many=True)
            response.data = serializer.data
        return response

class SeatDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Seat.objects.all()
    serializer_class = serializers.SeatSerializerRead
    permission_classes = (permissions.IsAuthenticated,)

    def put(self, request, pk, *args, **kwargs):
        try:
            seat = models.Seat.objects.get(pk=pk)
            edit_serializer = serializers.SeatSerializerWrite(seat, data=request.data, partial=True)
            if edit_serializer.is_valid():
                seat = edit_serializer.save()
                
                read_serializer = serializers.SeatSerializerRead(seat)
                return Response(data=read_serializer.data, status=status.HTTP_200_OK)
            else:
                instance = None
                return Response(data=edit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Seat.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)

    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            seat = models.Seat.objects.get(pk=pk)
            seat.soft_delete()
            serializer = serializers.SeatSerializerRead(seat)
            return Response(data=serializer.data, status=httpStatus)
        except models.Seat.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)


###################################### THEATRE API ######################################
class TheatreListAPI(generics.ListCreateAPIView):
    queryset = models.Theatre.objects.all()
    serializer_class = serializers.TheatreSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def create(self, request, *args, **kwargs):
        """
        {
            "row_count": 10,
            "column_count": 20,
            "seats": 200,
            "rest_time": 15
        }
        """
        write_serializer = serializers.TheatreSerializerWrite(data=request.data)
        if write_serializer.is_valid():
            theatre = write_serializer.save()
            theatre.create_theatre_seats()

            read_serializer = serializers.TheatreSerializerRead(theatre)
            return Response(data=read_serializer.data, status=status.HTTP_201_CREATED)
        else:
            instance = None
            return Response(data=write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TheatreDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Theatre.objects.all()
    serializer_class = serializers.TheatreSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def put(self, request, pk, *args, **kwargs):
        try:
            theatre = models.Theatre.objects.get(pk=pk)
            edit_serializer = serializers.TheatreSerializerWrite(theatre, data=request.data, partial=True)
            if edit_serializer.is_valid():
                theatre = edit_serializer.save()

                seats = models.Seat.objects.filter(theatre=theatre)
                for seat in seats:
                    seat.delete()
                theatre.create_theatre_seats()

                read_serializer = serializers.TheatreSerializerRead(theatre)
                return Response(data=read_serializer.data, status=status.HTTP_200_OK)
            else:
                instance = None
                return Response(data=edit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Theatre.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)
    
    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            theatre = models.Theatre.objects.get(pk=pk)
            theatre.soft_delete()
            serializer = serializers.TheatreSerializer(theatre)
            return Response(data=serializer.data, status=httpStatus)
        except models.Theatre.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)

###################################### SHOW API ######################################
class ShowListAPI(generics.ListCreateAPIView):
    queryset = models.Show.objects.all()
    serializer_class = serializers.ShowSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def create(self, request, *args, **kwargs):
        """
        {
            "schedule": 16/08/2021 14:00,
            "screening": 1,
            "theatre": 2,
        }
        """
        write_serializer = serializers.ShowSerializerWrite(data=request.data)
        if write_serializer.is_valid():
            show = write_serializer.save()

            read_serializer = serializers.ShowSerializerRead(show)
            return Response(data=read_serializer.data, status=status.HTTP_201_CREATED)
        else:
            instance = None
            return Response(data=write_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ShowDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Show.objects.all()
    serializer_class = serializers.ShowSerializerRead
    permission_classes = (IsAdminOrReadOnly,)

    def put(self, request, pk, *args, **kwargs):
        try:
            show = models.Show.objects.get(pk=pk)
            edit_serializer = serializers.ShowSerializerWrite(show, data=request.data, partial=True)
            if edit_serializer.is_valid():
                show = edit_serializer.save()

                read_serializer = serializers.ShowSerializerRead(show)
                return Response(data=read_serializer.data, status=status.HTTP_200_OK)
            else:
                instance = None
                return Response(data=edit_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except models.Show.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)
    
    def delete(self, request, pk, format=None):
        httpStatus = status.HTTP_200_OK
        try:
            show = models.Show.objects.get(pk=pk)
            show.soft_delete()
            serializer = serializers.ShowSerializer(show)
            return Response(data=serializer.data, status=httpStatus)
        except models.Show.DoesNotExist:
            httpStatus = status.HTTP_404_NOT_FOUND
            return Response(data=None, status=httpStatus)