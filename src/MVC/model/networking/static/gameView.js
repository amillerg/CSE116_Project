var socket = io.connect({transports: ['websocket']});
socket.on('gameState', myEvent);

function myEvent(event) {
    var gameState = JSON.parse(event);
    var playerslist = gameState["players"]
    var x = document.getElementById("players")
    x = playerslist.length



}