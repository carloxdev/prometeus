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

	$date_start_id = $('#id_date_start')
	$date_start_id.datepicker({
        format: 'dd/mm/yyyy',
		autoclose: true,
		clearBtn: true
    })

    $date_end_id = $('#id_date_end')
    $date_end_id.datepicker({
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
