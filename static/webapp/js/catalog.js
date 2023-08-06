var image_boxes = $(".image_box").map(function() {
    return this;
}).get();

let images = [];

for (const image_box of image_boxes){
    images.push(Array.from(image_box.children).filter(elem => elem.matches("img")));
}

let show_images = $(".image_to_show");

function swipe_right(prime_image, images, pointer){
    console.log(prime_image);
};
function swipe_left(prime_image, images, pointer){};

for (let i=0; i<images.length; i++){
    show_images[i].setAttribute("src", images[i][0].getAttribute("src"));
    show_images[i].setAttribute("id", 0);
    let left_pointer = $(show_images[i]).closest('div').find('.left_pointer')[0];
    let right_pointer = $(show_images[i]).closest('div').find('.right_pointer')[0];
    right_pointer.setAttribute('display', '');
    left_pointer.addEventListener("click", function(){swipe_left(show_images[i], images[i], left_pointer);});
    right_pointer.addEventListener("click", function(){swipe_left(show_images[i], images[i], right_pointer);});
}
