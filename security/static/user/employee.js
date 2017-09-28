/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// OBJS


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

    form_card = new FormCard()

})



/*-----------------------------------------------*\
            OBJETO: FormCard
\*-----------------------------------------------*/

function FormCard() {

    this.$recruited_date = $('#id_recruited_date')
    this.$birth_date = $('#id_birth_date')

    this.init_Components()
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
