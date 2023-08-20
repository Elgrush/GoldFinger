var delete_buttons = $('.delete_button');

for (const button of delete_buttons){
    button.addEventListener("click", function(){
    if (confirm('Вы уверены?'))
        $.ajax({
        type:'POST',
        url: window.location.href,
        data:
        {
            csrfmiddlewaretoken: $(button).closest('div').siblings('input[name="csrfmiddlewaretoken"]').val(),
            id: $(button).closest('div').siblings("#id_ArticleRequestId").val(),
        },
        success : function(res, status, xhr)
         {
            $(button).closest('div').closest('form').remove();
         }
        });
    });
}
