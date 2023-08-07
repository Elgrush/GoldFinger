var image_boxes = $(".image_box").map(function() {
    return this;
}).get();

$("*").find("img").map(function() {
    return this.setAttribute('loading', 'lazy');
});

let images = [];

for (const image_box of image_boxes){
    images.push(Array.from(image_box.children).filter(elem => elem.matches("img")));
}

let show_images = $(".image_to_show");

function swipe_right(prime_image, images, left_pointer, right_pointer){
    prime_image.id = Number(prime_image.id) + 1;
    prime_image.src = images[Number(prime_image.id)].src;
    if (Number(prime_image.id) == images.length-1){
        right_pointer.setAttribute('display', 'none');
    }
    left_pointer.setAttribute('display', '');
};
function swipe_left(prime_image, images, left_pointer, right_pointer){
    prime_image.id = Number(prime_image.id) - 1;
    prime_image.src = images[Number(prime_image.id)].src;
    right_pointer.setAttribute('display', '');
    if (Number(prime_image.id) == 0){
        left_pointer.setAttribute('display', 'none');
    }
};

for (let i=0; i<images.length; i++){
    if (images[i].length > 0){
        show_images[i].setAttribute("src", images[i][0].getAttribute("src"));
        show_images[i].setAttribute("id", 0);
        let left_pointer = $(show_images[i]).closest('div').find('.left_pointer')[0];
        let right_pointer = $(show_images[i]).closest('div').find('.right_pointer')[0];
        if (images[i].length > 1){
            right_pointer.setAttribute('display', '');
            }
        left_pointer.addEventListener("click", function(){swipe_left(show_images[i], images[i], left_pointer, right_pointer)});
        right_pointer.addEventListener("click", function(){swipe_right(show_images[i], images[i], left_pointer, right_pointer)});
        show_images[i].addEventListener("mouseover", function(){
            right_pointer.id = "";
            left_pointer.id = "";
        });
        left_pointer.addEventListener("mouseover", function(){
            right_pointer.id = "";
            left_pointer.id = "";
        });
        right_pointer.addEventListener("mouseover", function(){
            right_pointer.id = "";
            left_pointer.id = "";
        });
        show_images[i].addEventListener("mouseout", function(){
            right_pointer.id = "hoover_hide";
            left_pointer.id = "hoover_hide";
        });
    }
    else{
        show_images[i].closest('div').closest('form').removeChild(show_images[i].closest('div'));
    }
}
