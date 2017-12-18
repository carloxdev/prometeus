/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {
    formulario = new Form_edit()
})


Form_edit = function () {
    this.$form = $('#form_benefit_edit')
    this.$btn_submit = $('#btn_submit_edit')
    this.$payment_info = $('#id_payment_info')
    this.$payment_evidence = $('#id_payment_evidence')
    this.$admin_response = $('#id_admin_response')
    this.$status = $('#id_status')

    this.payment_info = this.$payment_info.val().trim()
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

    this.$btn_submit.on('click', this, this.validate_Form)
}

Form_edit.prototype.validate_Form = function (e) {
    var context = e.data
    if (context.$payment_info.val().trim() != '' && context.payment_info == '' && context.$status.val() == 'pen') {
        alertify.confirm('¿Deseas cambiar el estado de Pendiente a Pago Pendiente?', function (e) {
            context.$status.val('ppe')
            context.$form.submit()
        }, function (e) {
            context.$form.submit()
        })
    } else {
         context.$form.submit()
    }

    if (context.$admin_response.val().trim() != '' && context.admin_response == '' && context.$status.val() != 'com') {
        alertify.confirm('¿Deseas cambiar el estado a Completado?', function (e) {
            context.$status.val('com')
            context.$form.submit()
        }, function (e) {
            context.$form.submit()
        })
    } else {
         context.$form.submit()
    }
    return false
}