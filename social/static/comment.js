var input = null

$(document).ready(function () {

    input = new CommentsInput()

})

/* -------------------- OBJETO: CommentsInput -------------------- */

function CommentsInput() {
    this.$id = $('#comment_content')
    this.$button = $('#btn_enviar')

    this.set_Events()
}
CommentsInput.prototype.init = function () {

}
CommentsInput.prototype.set_Events = function () {
    this.$button.on("click", this, this.click_Enviar)
}
CommentsInput.prototype.click_Enviar = function (e) {
    alert("puto paquito")
}


/* -------------------- OBJETO: CommentsList -------------------- */

// function CommentsList() {
//     this.$id = $('#cabecera_pk')
// }
// CommentsList.prototype.init = function () {
//
// }
