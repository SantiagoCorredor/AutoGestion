document.addEventListener('DOMContentLoaded', function () {
    // Manejar el evento de clic en el botón de aplicar filtros
    var aplicarFiltrosButton = document.getElementById('aplicarFiltros');
    if (aplicarFiltrosButton) {
        aplicarFiltrosButton.addEventListener('click', function () {
            // Obtener los valores seleccionados de los filtros
            var filtrosSeleccionados = obtenerFiltrosSeleccionados();

            // Enviar los filtros a la vista de aplicar_filtros
            aplicarFiltros(filtrosSeleccionados);
        });
    }
});

function obtenerFiltrosSeleccionados() {
    var filtros = [];

    // Obtener el valor seleccionado del filtro de fecha
    var filtroFecha = document.getElementById('filtroFecha');
    if (filtroFecha) {
        var valorFecha = filtroFecha.value;
        filtros.push({ nombre: 'fecha', valor: valorFecha });
    }

    // Agregar más bloques de código según la cantidad y tipos de filtros que tengas

    return filtros;
}

function aplicarFiltros(filtros) {
    // Crear un objeto FormData para enviar los filtros al servidor
    var formData = new FormData();

    // Agregar cada filtro al objeto FormData
    for (var i = 0; i < filtros.length; i++) {
        formData.append('filtros[]', JSON.stringify(filtros[i]));
    }

    // Realizar una petición AJAX para enviar los filtros al servidor
    fetch('/aplicar_filtros/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        // Manejar la respuesta del servidor, por ejemplo, actualizar la tabla con los datos filtrados
        console.log(data);
    })
    .catch(error => {
        console.error('Error al aplicar filtros:', error);
    });
}
