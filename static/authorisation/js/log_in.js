let tg = window.Telegram.WebApp; //получаем объект webapp телеграма
var user = tg.initDataUnsafe.user.id;
var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
var theUrl = "?telegram_id="+user;
xmlhttp.open("GET", theUrl);
xmlhttp.send();
