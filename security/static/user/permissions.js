
/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    $grupos = $('#id_groups')

    $grupos.multiSelect({
        selectableHeader: "<div class='own-select-header'>Grupos disponibles</div>",
        selectionHeader: "<div class='own-select-header'>Grupos Asignados</div>",
    })

})
