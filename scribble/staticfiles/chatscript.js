<!--
//setup
$(document).ready( function() {
    window.chat = {};
    chat.ws = $.gracefulWebSocket("ws://dutch.mathcs.emory.edu:8026/ws");
    chat.send = function (message) {
      chat.ws.send(message);
}

var onlineUsers = [];
var anonymous = 0;


chat.ws.onmessage = function (event) {
  var messageFromServer = event.data;

 if(messageFromServer.charAt(0) === 'j')
 {
    var new_user = document.createElement('li');
    new_user.innerHTML = messageFromServer.substr(2);
    $("#user_list ul").append(new_user);

 }else if(messageFromServer.charAt(0) === 'l')
 {
     var user = document.getElementById(messageFromServer.substr(2));
     user.parentNode.removeChild(user);

 }else{

    var list_element = document.createElement('div');
    list_element.className = "row message";
    list_element.innerHTML = messageFromServer;

    //if this user sent the message move it to the right, make it purple
    if(messageFromServer.substr(2) === {{user}})
        new_user.style = "text-align:right; color:7C68A3;";

  $("#message_list ul").append(list_element);

   messages.scrollTop = messages.scrollHeight;
   }
};
function getLocation() {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(checkCoords);
        } else {
            alert("Geolocation is not supported by this browser.");
        }
    }

function checkCoords(position) {
    if(position.coords.latitude > 33.8 || position.coords.latitude < 33.6){
        if(position.coords.longitude > -84 ||  position.coords.longitude < -82){
            alert("You can't see this chat, please go away");
        }
    }
}


  chat.ws.onopen = function (event){
    chat.send("{{user}}:-:{{chat.name}}")
}


var messages = document.getElementById("message_list");



var inputBox = document.getElementById("inputbox");
inputbox.addEventListener("keydown", function(e) {
  if (!e) { var e = window.event; }
  if (e.keyCode == 13) {
    e.preventDefault(); // sometimes useful
    if(inputbox.value !== ""){
        chat.send("<b>{{user}}:</b> " + inputbox.value);
        inputbox.value="";
    }
  }
}, false);
});

function changeChat(){
    alert("You don't have permission to do that");
}


-->