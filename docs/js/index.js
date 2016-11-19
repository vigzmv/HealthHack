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
        $('.inputform1').slideUp('slow');
        $('.inputform2').slideUp('slow');
        $('.inputform3').slideUp('slow');
        $('.inputform4').slideUp('slow');

        if (selected == "Liver") {
            $('.inputform1').slideDown('slow');
        } else if (selected == "Heart") {
            $('.inputform2').slideDown('slow');
        } else if (selected == "Lungs") {
            $('.inputform3').slideDown('slow');
        } else if (selected == "Others") {
            $('.inputform4').slideDown('slow');
        }
    });

});
