let delete_buttons = $(".discard_item");

function menage_lot_item(delete_button, token){
    if(delete_button.value == "Убрать из корзины"){
        $.ajax({
            type:'POST',
            url: window.location.href.replace('shopping_cart', 'discard_item_from_cart'),
            data:
            {
                csrfmiddlewaretoken: token,
                id: $(delete_button).siblings("#id_CatalogItem_id").val(),
            },
            success : function(res, status, xhr)
             {
                 if (xhr.getResponseHeader("success") == 1){
                    delete_button.value = "Вернуть в корзину";
                 }
             }
        });
    }
    else{
        if(delete_button.value == "Вернуть в корзину"){
            $.ajax({
                type:'POST',
                url: window.location.href.replace('shopping_cart', 'add_item_to_cart'),
                data:
                {
                    csrfmiddlewaretoken: token,
                    id: $(delete_button).siblings("#id_CatalogItem_id").val(),
                    amount: $(delete_button).siblings(".amount_tools").children('#id_purchase_amount').val(),
                },
                success : function(res, status, xhr)
                 {
                     if (xhr.getResponseHeader("success") == 1){
                        delete_button.value = "Убрать из корзины";
                     };
                 }
               });
        }
    }
};

for (const delete_button of delete_buttons){
    let token = $(delete_button).siblings('input[name="csrfmiddlewaretoken"]').val();
    delete_button.addEventListener("click", function() {menage_lot_item(delete_button, token);});
}
