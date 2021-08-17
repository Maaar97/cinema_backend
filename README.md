CINEMA BACKEND

A Django project for managing a cinema, the software allows the user to manage the movies, the theatres and the shows on screening, also it allows user to buy tickets for the show they want.

The project has 3 apps:
    - Users
    This app manage the users and their access to the app, in it the defined models are:
        *Users:* stores the users data and their attributes will allow/deny the actions in the app.
    - Movies
    This app manage the movies and all the information related to them, in it the defined models are:
        *Actor:* stores the actors data, this will be linked to a movie.
        *Director:* stores the directos data, this will be linked to a movie and will be a filter attribute.
        *Genre:* stores the genres data, this will be linked to a movie and will be a filter attribute.
        *Format:* stores the movie formats data, this will set the price for a specific movie screening.
        *Movie:* stores the movies data.
        *Casting:* the middle table for the relation actor-movie.
        *Screening:* stablish the relation between movie and format, allowing a movie to have different formats to display.
    - Theatres
    This app manage the movie theatres and all the information related to them, in it the defined models are:
        *Seat:* stores the seats data, will be related to a specific theatre and it can be in different status.
        *Theatre:* stores the theatre data, will be related to a specific show.
        *Show:* stores the shows data, stablish the relation between a screening and a theatre, it has a specific datetime to start.
