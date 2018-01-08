
$(document).ready(function() {
    var $carrusel = $('#carrusel')
    $carrusel.slick({
        autoplay: true,
        autoplaySpeed: 3000,
        infinite: true,
        dots: true,

        responsive: [
            {
                breakpoint: 768,
                settings: {
                    dots: false,
                    arrows: false,
                }
            },
        ]
    })
})
