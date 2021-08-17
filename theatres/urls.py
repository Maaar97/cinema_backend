from . import views
from django.urls import path
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path(route='seat/', view=views.SeatListAPI.as_view(), name="Seats"),
    path(route='seat/<int:pk>/', view=views.SeatDetailAPI.as_view(), name="Seat"),

    path(route='theatre/', view=views.TheatreListAPI.as_view(), name="Theatres"),
    path(route='theatre/<int:pk>/', view=views.TheatreDetailAPI.as_view(), name="Theatre"),

    path(route='show/', view=views.ShowListAPI.as_view(), name="Shows"),
    path(route='show/<int:pk>/', view=views.ShowDetailAPI.as_view(), name="Show"),

]
