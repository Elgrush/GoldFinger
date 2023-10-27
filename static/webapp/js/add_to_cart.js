let add_buttons = $(".addToCartButton");

for (const add_button of add_buttons){
    let url = window.location.href+'webapp/add_item_to_cart/';
    add_button.addEventListener("click", function(){
        $.ajax({
        type:'POST',
        url: url.replace('webapp/webapp', 'webapp').replace('/webapp/catalog', ''),
        data:
        {
            csrfmiddlewaretoken: $(add_button).siblings('input[name="csrfmiddlewaretoken"]').val(),
            id: $(add_button).siblings("#id_CatalogItem_id").val(),
        },
        success : function(res, status, xhr)
         {
             if (xhr.getResponseHeader("success") == 1){
                add_button.value = "Добавлено";
             };
             if (xhr.getResponseHeader("success") == 0){
                add_button.value = "Уже в корзине";
             };
         }
        });
    });
}
