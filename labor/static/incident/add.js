/*------------- LOAD -------------*/

$(document).ready(function () {
	form = new Formulario()
})


/*------------- OBJETO: Formulario -------------*/

function Formulario() {
	this.$fecha = $('#id_date')
	this.$btn_submit = $('#btn_submit')

	this.init_Components()
	this.set_Events()
}
Formulario.prototype.init_Components = function () {

	this.$fecha.datepicker({
		format: 'dd/mm/yyyy',
		autoclose: true,
		clearBtn: true
	})
}
Formulario.prototype.set_Events = function () {
	this.$btn_submit.on("click", this, this.click_Submit)
}
Formulario.prototype.click_Submit = function (e) {
	Pace.restart()
}
