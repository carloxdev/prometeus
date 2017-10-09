
/* ------------------------ LOAD ------------------------ */

$(document).ready(function () {
    var $contenido =  $('#js-content')
    $contenido.find("img").addClass("img-responsive")
    $contenido.find("iframe").addClass("embed-responsive-item")
    $contenido.find("iframe").parent().addClass("embed-responsive embed-responsive-16by9")
})
