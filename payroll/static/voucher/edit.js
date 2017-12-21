/*------------- LOAD -------------*/

$(document).ready(function () {
	form = new Formulario()
})


/*------------- OBJETO: Formulario -------------*/

function Formulario() {
    this.$record_status = $('#record_status')
    this.$status = $('#id_status')
    this.$file =  $('.bootstrap-filestyle')
    this.$response = $('#id_response')

    this.init_Components()
}
Formulario.prototype.init_Components = function () {

    if (this.$record_status.text() == "can" || this.$record_status.text() == "com")
    {
        this.$status.attr('disabled', 'disabled')
        this.$file.hide()
        this.$response.attr('disabled', 'disabled')
    }
}
