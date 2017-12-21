/*------------- GLOBAL VARIABLES -------------*/

var galletita = Cookies.get('csrftoken')
var api_vouchertype = window.location.origin + "/api/vouchertype/"

/*------------- LOAD -------------*/

$(document).ready(function () {
	form = new Formulario()
})


/*------------- OBJETO: Formulario -------------*/

function Formulario() {
	this.$type = $('#id_type')
	this.$dates_section = $('#section_id_date_start')
	this.$date_start_id = $('#id_date_start')
	this.$date_end_id = $('#id_date_end')

    this.init_Components()
	this.set_Events()
}
Formulario.prototype.init_Components = function () {

	this.$date_start_id.datepicker({
        format: 'dd/mm/yyyy',
		autoclose: true,
		clearBtn: true
    })

    this.$date_end_id.datepicker({
        format: 'dd/mm/yyyy',
		autoclose: true,
		clearBtn: true
    })
}
Formulario.prototype.set_Events = function () {

	this.$type.on("change", this, this.change_Employee)
}
Formulario.prototype.change_Employee = function (e) {
	e.preventDefault()

	id = this.value
	api = api_vouchertype + id + "/"

	parent = e.data

	$.ajax({
		url: api,
		method: "GET",
		headers: { "X-CSRFToken": galletita },
		success: function (response) {
			if (response.valid_range == true) {
				parent.show_DateSection()
			}
			else {
				parent.hidden_DateSection()
			}
		},
		error: function (response) {
			alertify.error(response.responseJSON.detail)
		}
	})
}
Formulario.prototype.show_DateSection = function () {
	this.$dates_section.show()
}
Formulario.prototype.hidden_DateSection = function () {
	this.$dates_section.hide()
	this.$date_start_id.val("")
	this.$date_end_id.val("")
}
