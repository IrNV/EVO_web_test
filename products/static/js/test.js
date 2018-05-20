/*
Функция, которая реагирует на клик по картинке и с помощью AJAX отправляет
запрос с информацией о типе продукта (холодильник или телевизор) и
названии продукта
 */
$(document).ready(function () {
    // alert("Page is loaded")
    $( 'body' ).on( 'click', 'img', function () {
        // alert($(this).attr("class"))
        var type = $(this).attr("class")
        var name = $(this).attr("alt")
        $.ajax({
            type: "GET",
            url:"/products/click/"+type+"="+name,
        });
    });


}
)
