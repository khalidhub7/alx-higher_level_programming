const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

$.get(url, (data) => {
    data.films.forEach((filmUrl) => $.get(filmUrl, (film) => 
        $('#list_movies').append(`<li>${film.title}</li>`)));
});
