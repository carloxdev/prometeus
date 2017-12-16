/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {
    formulario = new Form_edit()
})


Form_edit = function () {
    this.$form = $('#form_benefit_edit')
    this.$payment_info = $('#id_payment_info')
    this.$payment_evidence = $('#id_payment_evidence')
    this.$admin_response = $('#id_admin_response')

    this.payment_info = this.$payment_info.val().trim()
    this.payment_evidence = this.$payment_evidence.val().trim()
    this.admin_response = this.$admin_response.val().trim()

    this.init()
}

Form_edit.prototype.init = function () {
    if (this.$payment_info.val().trim() == '') {
        this.$payment_evidence.parent().fadeOut()
        this.$admin_response.parent().fadeOut()
    } else if (this.$payment_evidence.val().trim() == '') {
        this.$admin_response.parent().fadeOut()
    }

    this.$form.on('submit', this, this.validate_Form)
}

Form_edit.prototype.validate_Form = function (e) {
    console.log('En desarollo...') // TODO: Falta agregar las validaciones para cambiar de estados.
}