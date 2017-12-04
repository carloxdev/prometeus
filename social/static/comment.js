var input = null
var galletita = Cookies.get('csrftoken')
var url_add_comment = window.location.origin + "/api/comments/add/"

$(document).ready(function () {

    input = new CommentsInput()
})

/* -------------------- OBJETO: CommentsInput -------------------- */

function CommentsInput() {
    this.$id = $('#comment_content')
    this.$button = $('#btn_enviar')

    this.set_Events()

}
CommentsInput.prototype.set_Events = function () {
    this.$button.on("click", this, this.click_Enviar)
}
CommentsInput.prototype.click_Enviar = function (e) {

    $.ajax({
        url: url_add_comment,
        data: {
            "object_type" : 'VoucherRequest',
            "object_id" : 
        },
        method: "POST",
        headers: { "X-CSRFToken": galletita },
        success: function (response) {
            // agregar comentario a la lista
            // alertify.success("Se agrego correctamente")
        },
        error: function (response) {
            alertify.error(response)
        }
    })
}


/* -------------------- OBJETO: CommentsList -------------------- */

// function CommentsList() {
//     this.$id = $('#cabecera_pk')
// }
// CommentsList.prototype.init = function () {
//
// }
