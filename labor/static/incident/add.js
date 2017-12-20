/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// OBJS


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {

	$employee = $('#id_employee')
	$employee.select2({
		theme: "bootstrap"
	})

	$fecha = $('#id_date')
	$fecha.datepicker({
		format: 'dd/mm/yyyy',
		autoclose: true,
		clearBtn: true
	})
})



/*-----------------------------------------------*\
            OBJETO: PostThree
\*-----------------------------------------------*/

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
