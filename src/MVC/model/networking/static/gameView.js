var socket = io.connect({transports: ['websocket']});
socket.on('gameState', myEvent);

function myEvent(event) {
    var gameState = JSON.parse(event);
    console.log(gameState)
    var playerslist = gameState["players"]
    var x = document.getElementById("players")
    x = playerslist.length



}