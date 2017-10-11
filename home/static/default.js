
$(document).ready(function() {
    var $carrusel = $('#carrusel')
    $carrusel.slick({
        autoplay: true,
        autoplaySpeed: 3000,
        infinite: true,
        dots: true,

        // centerMode: true,
        // centerPadding: '-10px',

        responsive: [
            // {
            //     breakpoint: 1024,
            //     settings: {
            //         slidesToShow: 3,
            //         slidesToScroll: 3,
            //     }
            // },
            {
                breakpoint: 600,
                settings: {
                    dots: false,
                    arrows: false,
                }
            },
            // {
            //     breakpoint: 480,
            //     settings: {
            //         dots: false,
            //         arrows: false,
            //
            //     }
            // }
            // You can unslick at a given breakpoint now by adding:
            // settings: "unslick"
            // instead of a settings object
        ]
    })
})
