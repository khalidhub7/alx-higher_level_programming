const url = "https://swapi-api.alx-tools.com/api/people/5/?format=json";

$.get(url, (data) => {
    let name = data.name;
    $("#character").text(name);
});
