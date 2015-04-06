<!--
//setup

        function addUser(text)
{
    var new_user = document.createElement('li');
    new_user.innerHTML = text;
    $("#user_list ul").append(new_user);
}

function removeUser(text)
{
    var user = document.getElementById(text);
    user.parentNode.removeChild(user);
}

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

function stripTags(text)
{
    var div = document.createElement("div");
    div.innerHTML = text;
    return div.textContent || div.innerText;
}

function changeChat()
{
    alert("You don't have permission to do that");
}

$(document).ready( function() {
    window.chat = {};
    var anonymous = 0;
    chat.ws = $.gracefulWebSocket("ws://45.55.163.213:8026/ws");

    chat.ws.onopen = function (event){
        chat.send("{{user}}:-:{{chat.name}}")
    };

    chat.send = function (message) {
      chat.ws.send(message);
    }


    chat.ws.onmessage = function (event) {
        var messageFromServer = event.data;

        if(messageFromServer.charAt(0) === 'j')
         {
            addUser(messageFromServer.substr(2));

            if(messageFromServer.substr(2) === "AnonymousUser")
                anonymous++;

        }else if(messageFromServer.charAt(0) === 'l')
        {
             removeUser(messageFromServer.substr(2));

             if(messageFromServer.substr(2) === "AnonymousUser")
                if(anonymous > 0)
                    anonymous--;
        }else{

        var list_element = document.createElement('div');
        list_element.className = "row message";
        list_element.innerHTML = messageFromServer;

        //when the user receives a message from themself move it to the right, color it purple, make it bold
        if(messageFromServer.substr(2) === "{{user}}" ){
            new_user.style = "text-align:right; color:7C68A3;";
            list_element.innerHTML = "<strong>"+list_element.innerHTML+"</strong>";
        }

        $("#message_list ul").append(list_element);

        messages.scrollTop = messages.scrollHeight;
       }
    };




    var messages = document.getElementById("message_list");
    var inputBox = document.getElementById("inputbox");

    inputbox.addEventListener("keydown", function(e) {
      if (!e) { var e = window.event; }
      if (e.keyCode == 13) {
        e.preventDefault(); // sometimes useful
        if(inputbox.value !== ""){

            //strip html tags
            var message = stripTags(inputBox.value);
            try{
                chat.send("<b>{{user}}:</b> " + message);
            }catch(err){
                alert(err);
            }
            inputbox.value="";
        }
      }
    }, false);
});


-->