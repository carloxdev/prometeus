
/* ------------------------ GLOBAL VARIABLES ------------------------ */
var form_card = null


/* ------------------------ LOAD ------------------------ */

$(document).ready(function () {

    form_card = new FormCard()

})



/* ------------------------ OBJETO: FormCard ------------------------ */

function FormCard() {

    this.$recruited_date = $('#id_recruited_date')
    this.$birth_date = $('#id_birth_date')

    this.$imagen = $('#id_photo')
    this.$imagen_preview = $('#img_preview')

    this.init_Components()
    this.init_Events()
}
FormCard.prototype.get_DateConfig = function () {
    return {
        format: 'dd/mm/yyyy',
        autoclose: true
    }
}
FormCard.prototype.init_Components = function () {

    this.$recruited_date.datepicker(this.get_DateConfig())
    this.$birth_date.datepicker(this.get_DateConfig())
}
FormCard.prototype.init_Events = function () {

    this.$imagen.on("change",this, this.set_PreviewImagen)
}
FormCard.prototype.set_PreviewImagen = function (e) {

    if (this.files && this.files[0]) {

        var reader = new FileReader()

        reader.onload = function (e) {
            form_card.$imagen_preview.attr('src', e.target.result)
        }

        reader.readAsDataURL(this.files[0])

    }
}

// function PostThree() {

//     this.id = $('#myTree')

//     this.init_Components()
// }
// PostThree.prototype.init_Components = function () {

//     // dataSource = function(parentData, callback){
//     //   //...
//     // };

//     this.id.tree()

// }
