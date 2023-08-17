const current_forms = document.getElementsByClassName("request_form");

function answer(form) {}

function send_request(form, button) {
    $.ajax({
    type:'POST',
    url: window.location.href,
    data:
    {
        csrfmiddlewaretoken: form.querySelector('input[name="csrfmiddlewaretoken"]').value,
        amount: form.querySelector(".answer_amount").value,
        price: form.querySelector(".answer_price").value,
        ArticleRequestId: form.querySelector('input[name="ArticleRequestId"]').value
    },
    success:function(){
          button.form.removeChild(button);
          button = document.createElement("input");
                button.type = "button";
                button.value = "Изменить ответ";
                button.addEventListener("click", function(){
                answer(form)
                });
                form.appendChild(button);
            }
    });
};

function answer(form) {
    let children = $(form).children();
    let child;
    child = children.filter('.answer_amount')[0];
    child.removeAttribute('readonly');
    if (child.getAttribute('style') != null){
        child.removeAttribute("style");
        let field = child.cloneNode(true);
        child.form.removeChild(child);
        let label = document.createElement("label");
        label.setAttribute('for', "id_amount");
        label.textContent = "В наличии:";
        form.appendChild(label);
        form.appendChild(field);
    }
    child = children.filter('.answer_price')[0];
    child.removeAttribute('readonly');
    if (child.getAttribute('style') != null){
        child.removeAttribute("style");
        let field = child.cloneNode(true);
        child.form.removeChild(child);
        let label = document.createElement("label");
        label.setAttribute('for', "id_price");
        label.textContent = "Цена:";
        form.appendChild(label);
        form.appendChild(field);
    }
    child = children.filter('.answer_amount')[0];
    for (child of form.children){
        if (child.type == "button"){
            child.form.removeChild(child);
            break;
            }
    }
    const button = document.createElement("input");
    button.type = "button";
    button.value = "Подтвердить";
    button.addEventListener("click", function(){send_request(form, button)});
    form.appendChild(button);
};

for (const form of current_forms){
    var last_field;
    for (const child of form.children) {
        if (child.className == "answer_amount"){
            if (child.value == ""){
                let button = document.createElement("input");
                button.type = "button";
                button.value = "Ответить на запрос";
                button.addEventListener("click", function(){
                answer(form)
                });
                form.appendChild(button);
            }
            else{
                let button = document.createElement("button");
                button.textContent  = "Изменить ответ";
                button.type = "button";
                button.addEventListener("click", function(){
                answer(form)
                });
                form.appendChild(button);
            }
        }
    }
}
