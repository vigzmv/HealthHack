var selected = ""

$(document).ready(function() {

    $(".selLabel").click(function() {
        $('.dropdown').toggleClass('active');
    });

    $(".dropdown-list li").click(function() {
        $('.selLabel').text($(this).text());
        $('.dropdown').removeClass('active');
        $('#select-heading').slideUp('slow');

        selected = $('.selLabel').text().trim();
        console.log(selected);
        if (selected == "Liver") {
            $('.inputform1').slideDown('slow');
            $('.inputform2').slideUp('slow');
            $('.inputform3').slideUp('slow');
        } else if (selected == "Heart") {
            $('.inputform1').slideUp('slow');
            $('.inputform2').slideDown('slow');
            $('.inputform3').slideUp('slow');
        } else if (selected == "Lungs") {
            $('.inputform1').slideUp('slow');
            $('.inputform2').slideUp('slow');
            $('.inputform3').slideDown('slow');
        }
    });

});
