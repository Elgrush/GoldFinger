let return_to_catalog_button = document.getElementById('back_to_catalog_id');
let confirm_button = $('.confirm_button');

function report(){
    for(amount_field of $(("#id_purchase_amount"))){
        $.ajax({
        type:'POST',
        url: window.location.href.replace('shopping_cart', 'set_cart_amount'),
        data:
        {
            csrfmiddlewaretoken: $(amount_field).closest('div').siblings('input[name="csrfmiddlewaretoken"]').val(),
            id: $(amount_field).closest('div').siblings("#id_CatalogItem_id").val(),
            amount: amount_field.value,
        }
        });
    }
}

confirm_button.bind('click', function(){report()});
return_to_catalog_button.addEventListener('click', function(){report()});
