const url = "https://hellosalut.stefanbohacek.dev/?lang=fr";

$.get(url, (data) => {
    const neww = data.hello;
    $("#hello").text(neww);
});
