let amount_fields = $("#id_amount");

let purchase_amount_fields = $("#id_purchase_amount");

for (i of [...Array(amount_fields.length).keys()]){
    purchase_amount_fields[i].removeAttribute('readonly');
    purchase_amount_fields[i].setAttribute('min', '0');
    purchase_amount_fields[i].setAttribute('max', amount_fields[i].value);
}
