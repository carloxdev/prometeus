/*------------- GLOBAL VARIABLES -------------*/
var api_incidentevidence = window.location.origin + "/api/incidentevidence/"
var form = null

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
		sequentialUploads: true,
		replaceFileInput: false,
	    start: function (e) {
	    	$("#modal-progress").modal("show")
	    },
	    stop: function (e) {
	      	$("#modal-progress").modal("hide")
	    },
	    progressall: function (e, data) {
	      	var progress = parseInt(data.loaded / data.total * 100, 10)
	      	var strProgress = progress + "%"
	      	$(".progress-bar").css({"width": strProgress})
	      	$(".progress-bar").text(strProgress)
	    },
        done: this.show_FileUploaded,
        error: function (response) {
			mensaje = ""
			$.each(response.responseJSON, function (indice, elemento) {
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
    form.$empty_section.hide()
    form.$gallery.find('tbody').prepend(
		"<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
	)
}
Formulario.prototype.click_btn_upload = function (e) {
    e.data.$fileupload.click()
}
