/*------------- GLOBAL VARIABLES -------------*/
var api_incidentevidence = window.location.origin + "/api/incidentevidence/"

/*------------- LOAD -------------*/

$(document).ready(function () {
	form = new Formulario()
})


/*------------- OBJETO: Formulario -------------*/

function Formulario() {

    this.$btn_upload = $("#btn-upload")
    this.$fileupload = $("#fileupload")
    this.$empty_section = $("#empty-section-message")
    this.$gallery = $("#gallery")

    this.init_Components()
    this.set_Events()
}
Formulario.prototype.init_Components = function () {
    this.$fileupload.fileupload({
        dataType: 'json',
        url: api_incidentevidence,
        done: this.show_FileUploaded,
        error: function (response) {
			mensaje = ""
			$.each(response.responseJSON, function (indice, elemento) {
			  	console.log('¡Hola :' + elemento + '!');
				mensaje = mensaje + indice + " :" + elemento[0] + "\n"
			})

			alertify.error(mensaje)
        }
    })
}
Formulario.prototype.set_Events = function () {
    this.$btn_upload.on("click", this, this.click_btn_upload)
}
Formulario.prototype.show_FileUploaded = function (e, data) {
    this.$empty_section.hide()
    alert("Awebo")
}
Formulario.prototype.click_btn_upload = function (e) {
    e.data.$fileupload.click()
}
