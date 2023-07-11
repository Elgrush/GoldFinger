function findLableForControl(el) {
   var idVal = el.id;
   labels = document.getElementsByTagName('label');
   for( var i = 0; i < labels.length; i++ ) {
      if (labels[i].htmlFor == idVal)
           return labels[i];
   }
}

function hideField(field, label){
    field.setAttribute('style', "display: none");
    label.setAttribute('style', "display: none");
    field.required = false;
}

function revealField(field, label){
    field.style = false;
    label.style = false;
    field.required = true;
}

const size_field = document.getElementById("id_size");

const size_label = findLableForControl(size_field);

const hide_array = ["Подвеска", "Серьги"];

const type_box = document.getElementById("id_type");

if (hide_array.includes(type_box.options[type_box.selectedIndex].text)){
    hideField(size_field, size_label);
}
else{
    size_field.required = true;
}

type_box.addEventListener('change', function() {
  if (hide_array.includes(type_box.options[type_box.selectedIndex].text)) {
    hideField(size_field, size_label);
  }
  else{
    revealField(size_field, size_label);
  }
});
