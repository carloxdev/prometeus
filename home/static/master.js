
/* ------------------------ LOAD ------------------------ */

$(document).ready(function () {
    window.paceOptions = {
        // Disable the 'elements' source
        elements: true,
        // Only show the progress on regular and ajax-y page navigation,
        // not every request
        restartOnRequestAfter: true,
        ajax: {
          trackMethods: ['GET', 'POST', 'DELETE', 'PUT', 'PATCH']
        }
    }
})
