let price_fields = $(".price_class");
let purchase_amount_fields = $(".purchase_amount_class");
let amount_fields = $(".amount_class");
let final_price_field = $("#id_final_price")

function calculate_total(){
    let result_price = 0;
    for (i of [...Array(price_fields.length).keys()]){
        let button;
        for (button of price_fields[i].parentNode.children){
            if(button.getAttribute('class') == 'discard_item'){
                break;
            }
        }
        if(button.getAttribute('value') == 'Убрать из корзины'){
            result_price += price_fields[i].value * purchase_amount_fields[i].value;
        }
    }
    final_price_field.val(result_price);
}

for (i of [...Array(amount_fields.length).keys()]){
    purchase_amount_fields[i].removeAttribute('readonly');
    purchase_amount_fields[i].setAttribute('min', '0');
    purchase_amount_fields[i].setAttribute('max', amount_fields[i].value);
    purchase_amount_fields[i].addEventListener('change', calculate_total);
    let button;
    for (button of price_fields[i].parentNode.children){
        if(button.getAttribute('class') == 'discard_item'){
            break;
        }
    }
    button.addEventListener('click', function() {setTimeout(function() {
      calculate_total();
    }, 300);} );
}

calculate_total();
