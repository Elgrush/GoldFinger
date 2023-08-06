function delete_image_row(p){
    id = 0;
    const container = p.parentNode;
    container.removeChild(p);
    for (const child of container.children){
        if (child.className == "image_field"){
            var subChild;
            for (subChild of child.children){
                if(subChild.className == "jewelery_image"){
                    break
                }
            }
            subChild.setAttribute('id', 'id_image_input_' + id);
            subChild.setAttribute('name', 'image_' + id);
            id += 1;
        }
    }
}

function add_image_row(container){
    let image_input = document.createElement("input");
    id += 1;
    image_input.setAttribute('id', 'id_image_input_' + id);
    image_input.setAttribute('name', 'image_' + id);
    image_input.setAttribute('class', "jewelery_image");
    image_input.setAttribute('type', "file");
    image_input.setAttribute('accept', "image/*");

    let p = document.createElement("p");
    p.setAttribute('class', "image_field");
    p.appendChild(image_input);

    let delete_button = document.createElement("input");
    delete_button.setAttribute('class', "delete_image");
    delete_button.type = "button";
    delete_button.value = "X";
    delete_button.addEventListener("click", function(){delete_image_row(p)});
    p.appendChild(delete_button);

    container.appendChild(p);
}

var id = 0;

const button = document.createElement("input");
button.setAttribute('class', "add_image");
button.type = "button";
button.value = "Добавить фото";
const form = document.getElementById("lot_form");
button.addEventListener("click", function(){add_image_row(document.getElementById("image_box"))});
form.appendChild(button);
