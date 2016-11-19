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
        $('.strike').slideDown('slow');
        $('.animated').slideDown('slow');
        $('.form').slideDown('slow');

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
$("form").on("change", ".file-upload-field", function() {
    $(this).parent(".file-upload-wrapper").attr("data-text", $(this).val().replace(/.*(\/|\\)/, ''));
});

function getresponse(){
    $.ajax(
	{
	    type: 'POST',
	    url: 'http://localhost:5000/',
	    data: {text:query},
	    success: function(data)
	    {
	        console.log(data);
	        return data;
	    },
	    error: function()
	    {
			return "API RESPONSE is NULL"
	    }
	});
}

function pageLoad() {
    document.getElementById("Send").addEventListener('click', getresponse, false);
};

window.addEventListener('load', pageLoad, false);
