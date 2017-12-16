var filter_checkbox = null
var cookie_filter = false
/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {
    try {
        filter_checkbox = $('#filter_checkbox')
        cookie_filter = Cookies.get('filter_checkbox')
    } catch (err) {
        console.log('unable to get checkbox filter')
    }

    if (filter_checkbox) {
        filter_checkbox.prop('checked', Boolean(cookie_filter))
        filter_checkbox.on('change', function (e) {
            if ($(e.target).prop('checked')) {
                Cookies.set('filter_checkbox', 1, {expire: 7})
            } else {
                Cookies.remove('filter_checkbox')
            }
            window.location.reload()
        })
    }
})