let add_buttons = $(".add_button");

for (const add_button of add_buttons){
    let url = window.location.href.replace('request_history', 'add_request_to_cart');
    add_button.addEventListener("click", function(){
        $.ajax({
        type:'POST',
        url: url,
        data:
        {
            csrfmiddlewaretoken: $(add_button).siblings('input[name="csrfmiddlewaretoken"]').val(),
            id: $(add_button).siblings("#id_ArticleRequestAnswerId").val(),
        },
        success : function(res, status, xhr)
         {
             if (xhr.getResponseHeader("success") == 1){
                add_button.value = "Добавлено";
             };
             if (xhr.getResponseHeader("success") == 0){
                add_button.value = "Уже в корзине";
             };
             if (xhr.getResponseHeader("success") == -1){
                add_button.value = "Ответ ещё не получен";
             };
         }
        });
    });
}
