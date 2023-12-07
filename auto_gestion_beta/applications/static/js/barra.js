document.addEventListener("DOMContentLoaded", function () {
    // Botón para desplegar/colapsar la barra lateral
    var toggleButton = document.getElementById("toggle-sidebar");
    // Barra lateral
    var sidebar = document.getElementById("sidebar");
    
    // Manejador de eventos para el botón
    toggleButton.addEventListener("click", function () {
        // Cambiar la posición de la barra lateral al hacer clic en el botón
        if (sidebar.style.left === "0px" || sidebar.style.left === "") {
            sidebar.style.left = "-275px"; // Ocultar la barra lateral
        } else {
            sidebar.style.left = "0px"; // Mostrar la barra lateral
        }
    });
});
