/*-----------------------------------------------*\
            GLOBAL VARIABLES
\*-----------------------------------------------*/

// OBJS


/*-----------------------------------------------*\
            LOAD
\*-----------------------------------------------*/

$(document).ready(function () {
  
	$empleados = $('#empleados')
	$empleados.select2({
		theme: "bootstrap"
	})

	$fecha = $('#fecha')
	
    $fecha.datepicker()
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