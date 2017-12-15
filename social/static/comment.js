var input = null
var galletita = Cookies.get('csrftoken')
var url_add_comment = window.location.origin + "/api/comments/add/"

$(document).ready(function () {

    moment.locale('es');

    input = new CommentsInput()
})

/* -------------------- OBJETO: CommentsInput -------------------- */

function CommentsInput() {
    this.$content = $('#comment_content')
    this.$object_id = $('#object_id')
    this.$tag_model = this.$object_id.data('tag-model')
    this.$button = $('#btn_enviar')
    this.$user = $('#user')
    this.$list_comments = $('#list_comments')

    this.set_Events()
}
CommentsInput.prototype.set_Events = function () {
    this.$button.on("click", this, this.click_Enviar)
}
CommentsInput.prototype.click_Enviar = function (e) {

    obj = e.data

    if (obj.$content.val() == "") {
        alertify.alert('Favor de especificar un comentario');
    }
    else {
        $.ajax({
            url: url_add_comment,
            data: {
                "object_type" : obj.$tag_model,
                "object_id" : obj.$object_id.text(),
                "comment" :  obj.$content.val()
            },
            method: "POST",
            headers: { "X-CSRFToken": galletita },
            success: function (response) {
                date = moment(response.fecha).fromNow()
                obj.add_Comment(obj.$user.text(), response.contenido, date)
                obj.$content.val("")
                alertify.success("Se agrego tu comentario con exito")
            },
            error: function (response) {
                alertify.error(response.responseJSON.detail)
            }
        })
    }
}
CommentsInput.prototype.add_Comment = function (_user, _comment, _date) {
    var newElement = $('<div>' ,
        {
            html: "<div class='panel panel-default'>" +
                    "<div class='panel-heading'>" +
                        "<span class='badge'>" + _user + "</span> comento " + _date + ":" +
                    "</div>" +
                        "<div class='panel-body'>" +
                            _comment +
                        "</div>" +
                    "</div>"
        }
    )
    this.$list_comments.prepend(newElement);
}
