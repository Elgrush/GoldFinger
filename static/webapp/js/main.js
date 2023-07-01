let tg = window.Telegram.WebApp; //получаем объект webapp телеграма
var abtn = document.getElementById("abutton");
var aartin = document.getElementById("aarticle");
var asiin = document.getElementById("asize");
var aamin = document.getElementById("aamount");
abtn.addEventListener('click',function(){
 var article = aartin.value;
 var size = asiin.value;
 var amount = aamin.value;
 var user = tg.initDataUnsafe.user.id;
 if(!article){
    alert("Введите, пожалуйста артикул")
     }
 else{
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    var theUrl = "dispatcher/makeArticleRequest/";
    xmlhttp.open("POST", theUrl);
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.send(JSON.stringify({ "article": article, "size": size, "amount": amount, "user": user }));
    }
})