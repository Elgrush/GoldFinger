let all_amount_tools = $(".amount_tools");

for (amount_tools of all_amount_tools){
    $(amount_tools.children).filter('.minus').on('click', function(){
        let purchase_amount_field =  $(this).siblings().filter('#id_purchase_amount');
        if(Number($(purchase_amount_field).val())-1 >= Number(purchase_amount_field[0].getAttribute("min"))){
            $(purchase_amount_field).val(Number($(purchase_amount_field).val())-1);
        }
    });
    $(amount_tools.children).filter('.plus').on('click', function(){
        let purchase_amount_field = $(this).siblings().filter('#id_purchase_amount');
        if(Number($(purchase_amount_field).val())+1 <= Number(purchase_amount_field[0].getAttribute("max"))){
            $(purchase_amount_field).val(Number($(purchase_amount_field).val())+1);
        }
    });
}
