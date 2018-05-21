/*
Функция, которая реагирует на клик по картинке и с помощью AJAX отправляет
запрос с информацией о типе продукта (холодильник или телевизор) и
названии продукта
 */
$(document).ready(function () {
    $( 'body' ).on( 'click', 'img', function () {
        var type = $(this).attr("class");
        var name = $(this).attr("alt");
        var click_info = {'type': type, 'name': name};
        $.ajax({
            type: "POST",
            url:"/products/click",
            data: JSON.stringify(click_info),
            contentType: "/products/click/json",
            success: function () {
                window.location.reload(true)
            }
        });
    });


}
)
