const delete_button = document.getElementById("submit_form");
const storage_box = document.getElementById("image_box");
const change_counter = 0;

function deleteRequest(id){
    $.ajax({
    type:'POST',
    url: window.location.href.replace('edit_lot','delete_image'),
    data:
    {
        csrfmiddlewaretoken: form.querySelector('input[name="csrfmiddlewaretoken"]').value,
        id: id
    }
    });
}

function report_delete(){
    for (const box of storage_box.children){
            var id = 0;
            for (const element of box.children){
                if(element.id == "delete_checkbox"){
                    for(const subElement of element.children){
                        if(subElement.nodeName == "INPUT"){
                            if(subElement.checked){
                                deleteRequest(id);
                            }
                        }
                    }
                }
                else{
                    if(element.nodeName == "INPUT"){
                        if(element.files.length > 0){
                            deleteRequest(id);
                            element.name = 'swap_image_' + id;
                        }
                    }
                    if(element.nodeName == "DIV"){
                        for(const id_field of element.children){
                            if(id_field.nodeName == "INPUT"){
                                id = id_field.value;
                                console.log(id);
                            }
                        }
                    }
                }
            }
    }
}

delete_button.addEventListener("click", function(){
    report_delete();
})
