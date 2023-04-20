document.addEventListener("DOMContentLoaded", function () {
    var input = document.querySelector('input[type="submit"]');

    input.addEventListener('click', function () {
        // Aquí puede agregar el código que se ejecutará cuando se haga clic en el botón de envío.
        const id = document.querySelector('#identificacion').value;
        const nombre = document.querySelector('#nombre').value;
        const edad = document.querySelector('#edad').value;
        const gmail = document.querySelector('#gmail').value;

        const datos = {
            id: id,
            nombre: nombre,
            edad: edad,
            gmail: gmail
        };

        const datosJson = JSON.stringify(datos);
        console.log(datosJson)
        alert(datosJson);

        fetch('http://localhost:2080/api/datos/new', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: datosJson
        })
            .then(response => response.json())
            .then(data => console.log(data))
            .catch(error => console.error(error));

    });


});
