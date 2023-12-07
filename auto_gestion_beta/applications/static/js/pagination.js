document.addEventListener("DOMContentLoaded", function() {
    // Obtén el número de página actual de la URL (si existe)
    const urlParams = new URLSearchParams(window.location.search);
    const currentPage = parseInt(urlParams.get('page')) || 1;

    const tabsContainer = document.getElementById('tabs-container');
    const pageButtonsContainer = document.getElementById('page-buttons-container');
    const totalPages = parseInt(document.getElementById('last-button').dataset.page);

    function updateTab(currentPage) {
        // Remueve la clase 'active' de todas las pestañas
        let tabs = tabsContainer.getElementsByTagName('button');
        for (let i = 0; i < tabs.length; i++) {
            tabs[i].classList.remove('active');
        }

        // Agrega la clase 'active' a la pestaña de la página actual
        tabs[currentPage - 1].classList.add('active');
    }

    function refreshTable(currentPage) {
        const rowsPerPage = 50; // Cambia esto si es necesario
        const start_index = (currentPage - 1) * rowsPerPage;
        const end_index = currentPage * rowsPerPage;

        let rows = document.querySelectorAll('.table tbody tr');
        rows.forEach((row, index) => {
            if (index >= start_index && index < end_index) {
                row.style.display = 'table-row';
            } else {
                row.style.display = 'none';
            }
        });
    }

    function generatePageButtons(currentPage, totalPages) {
        const pageButtons = document.querySelectorAll('.page-button');
        pageButtons.forEach(button => {
            pageButtonsContainer.removeChild(button);
        });
    
        const visiblePages = 5; // Ajusta el número de páginas adyacentes a mostrar
        let startPage = Math.max(currentPage - visiblePages, 1);
        let endPage = Math.min(currentPage + visiblePages, totalPages);
    
        const tabsContainer = document.getElementById('tabs-container'); // Asegúrate de que 'tabs-container' exista
        if (tabsContainer) {
            // Realiza la lógica de actualización de pestañas aquí
        }
        
        for (let i = startPage; i <= endPage; i++) {
            const pageButton = document.createElement('button');
            pageButton.textContent = i;
            pageButton.dataset.page = i;
            pageButton.classList.add('page-button');
            if (i === currentPage) {
                pageButton.classList.add('active');
            }
            pageButtonsContainer.appendChild(pageButton);
        }
    }
    
    

    refreshTable(currentPage);
    generatePageButtons(currentPage, totalPages);
    updateTab(currentPage);
});
