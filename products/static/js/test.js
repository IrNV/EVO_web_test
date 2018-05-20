/*
Функция, которая реагирует на клик по картинке и с помощью AJAX отправляет
запрос с информацией о типе продукта (холодильник или телевизор) и
названии продукта
 */
$(document).ready(function () {
    $( 'body' ).on( 'click', 'img', function () {
        alert("Вы сделали клик по " + $(this).attr("alt"))
        var type = $(this).attr("class")
        var name = $(this).attr("alt")
        $.ajax({
            type: "GET",
            url:"/products/click/"+type+"="+name,
        });
    });


}
)
