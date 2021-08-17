from . import views
from django.urls import path
from rest_framework.authtoken import views as auth_views

urlpatterns = [
    path(route='actor/', view=views.ActorListAPI.as_view(), name="Actors"),
    path(route='actor/<int:pk>/', view=views.ActorDetailAPI.as_view(), name="Actor"),

    path(route='director/', view=views.DirectorListAPI.as_view(), name="Directors"),
    path(route='director/<int:pk>/', view=views.DirectorDetailAPI.as_view(), name="Director"),

    path(route='genre/', view=views.GenreListAPI.as_view(), name="Genres"),
    path(route='genre/<int:pk>/', view=views.GenreDetailAPI.as_view(), name="Genre"),

    path(route='movie/', view=views.MovieListAPI.as_view(), name="Movies"),
    path(route='movie/<int:pk>/', view=views.MovieDetailAPI.as_view(), name="Movie"),

    path(route='format/', view=views.FormatListAPI.as_view(), name="Formats"),
    path(route='format/<int:pk>/', view=views.FormatDetailAPI.as_view(), name="Format"),

    path(route='screening/', view=views.ScreeningListAPI.as_view(), name="Screenings"),
    path(route='screening/<int:pk>/', view=views.ScreeningDetailAPI.as_view(), name="Screening"),
]
