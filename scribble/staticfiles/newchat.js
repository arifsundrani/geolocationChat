<!--
//setup

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
    document.getElementById("lat").value = Math.round(lat);
    document.getElementById("long").value = Math.round(long);
  }


$(document).ready( function() {
    getLocation();
});













-->