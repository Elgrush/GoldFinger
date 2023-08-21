var parse_button = $('.parse_button');
var article_field = $('#article_id')

parse_button.on('click', function(){
     $.ajax({
        type:'POST',
        url: window.location.href.replace('parse', 'parser'),
        data:
        {
            csrfmiddlewaretoken: article_field.siblings('input[name="csrfmiddlewaretoken"]').val(),
            article: article_field.val(),
        },
        success : function(res, status, xhr)
         {

         }
        });
})
