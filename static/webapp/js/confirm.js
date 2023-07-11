function findLableForControl(el) {
   var idVal = el.id;
   labels = document.getElementsByTagName('label');
   for( var i = 0; i < labels.length; i++ ) {
      if (labels[i].htmlFor == idVal)
           return labels[i];
   }
}

const size_field = document.getElementById("id_size");

const size_label = findLableForControl(size_field);

if (size_field.getAttribute('style') == "display: none"){
    size_label.setAttribute('style', "display: none");
}
