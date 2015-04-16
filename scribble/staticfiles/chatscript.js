
//setup
//functions
function sendMessage(message, user)
{
    var resp = {};
    resp.type = "message";
    resp.content = message;
    resp.sender = user;
    chat.send(JSON.stringify(resp));
}


function joinChat(user, pk)
{
    var resp = {};
    resp.type = "join";
    resp.content = {"userName" : user, "room" : pk};
    resp.sender = "system";
    chat.send(JSON.stringify(resp));
}

function leaveChat(user)
{
    var resp = {};
    resp.type = "leave";
    resp.content = [];
    resp.content['userName'] = user;
    resp.content['room'] = chat.pk;
    resp.sender = "system";
    chat.send(JSON.stringify(resp));
}

function flagUser(who, user)
{
    var resp = {};
    resp.type = "flag";
    resp.content = who;
    resp.sender = user;
    chat.send(JSON.stringify(resp));
}

function addUser(text)
{
    var new_user = document.createElement('li');
    new_user.innerHTML = text;
    $("#user_list ul").append(new_user);
}

function removeUser(text, user)
{
    var user = document.getElementById(text);
    user.parentNode.removeChild(user);
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

var long;
var lat;
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    }
}

function showPosition(position) {
    lat = parseFloat(position.coords.latitude);
    long = parseFloat(position.coords.longitude);


//    console.log("lat is " + lat + " and long is " + long);
    var lats = document.getElementsByClassName("lat");
    for(var i = 0; i < lats.length; i++)
    {
        lats[i].value = lat;
    }

    var longs = document.getElementsByClassName("long");
    for(var i = 0; i < lats.length; i++)
        longs[i].value = long;
    //setTimeout(getLocation,500);
  }


$(document).ready( function() {
    getLocation();
    window.chat = {};
    usersOnline = [];
    var anonymous = 0;
    var user = document.getElementById("hold_user").innerHTML;
    var pk = document.getElementById("hold_pk").innerHTML;
    var obj;
    chat.ws = $.gracefulWebSocket("ws://45.55.163.213:8026/ws");
    //ws://10.40.83.74:8026/ws
    chat.ws.onopen = function (event){
        joinChat(user, pk);
        //chat.send("{{user}}:-:{{chat.name}}")
    };

    chat.send = function (message) {
        chat.ws.send(message);
    }


    chat.ws.onmessage = function (event) {

        console.log("data: "+event.data)
        obj = JSON.parse(event.data);


        if(obj.type === 'join')
         {
            if(! (obj.content.userName in usersOnline))
            {
                if(obj.content.userName !== "AnonymousUser")
                    addUser(obj.content.userName);
                usersOnline.push(obj.content.userName);
            }


            if(obj.content.userName === "AnonymousUser"){
                anonymous++;
                document.getElementById('numAnon').innerHTML = anonymous;
            }

        }else if(obj.type === "leave")
        {
             removeUser(obj.content.userName);

             if(obj.content.userName === "AnonymousUser")
                if(anonymous > 0){
                    anonymous--;
                    document.getElementById('numAnon').innerHTML = anonymous;
                }

            leaveChat(obj.content.userName);
        }else{

        var list_element = document.createElement('div');
        list_element.className = "row message";
        list_element.innerHTML = "<strong>" + obj.sender + ":</strong> "+obj.content;

        //when the user receives a message from themself move it to the right, color it purple, make it bold
//        if(messageFromServer.substr(2) === "{{user}}" ){
//            list_element.style = "text-align:right; color:7C68A3;";
//            list_element.innerHTML = "<strong>"+list_element.innerHTML+"</strong>";
//        }

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

            if(message.toLowerCase().indexOf("fuck") != -1 || message.toLowerCase().indexOf("penis") != -1 || message.toLowerCase().indexOf("pussy") != -1 || message.toLowerCase().indexOf("dick") != -1 || message.toLowerCase().indexOf("bitch") != -1
            || message.toLowerCase().indexOf("shit") != -1){
                alert("you're rude!");
                inputbox.value="I use vulgar language";
            }
            else{
                sendMessage(message, user);
                inputbox.value="";
            }
        }
      }
    }, false);
});

