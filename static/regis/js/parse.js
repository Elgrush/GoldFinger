var parse_button = $('.parse_button');
var article_field = $('#article_id')

parse_button.on('click', function(){
      parse_button.remove();
      article_field.prop('readonly', true);
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
            let data = JSON.parse(xhr.getResponseHeader("data"));
            $('.parse_box').add('<p>'+ data['text'] +'</p>'
            ).appendTo('main');
            for (const src of data['images']){
                $('.parse_box').add('<img src='+ src +'>'
                ).appendTo('main');
            }
            article_field.remove();
            $('label').remove();
        }
        });
})
