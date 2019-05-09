var socket = io.connect({transports: ['websocket']});
socket.on('gameState', myEvent);

var canvas = document.getElementById("canvas");
var context = canvas.getContext("2d");
context.globalCompositeOperation = 'source-over';

canvas.width = 1200;
canvas.height = 600;


var background = new Image();
background.src = "https://www.psdgraphics.com/file/night-sky-stars.jpg";

background.onload = function(){
    context.drawImage(background,0,0);
}


function myEvent(event) {
    var gameState = JSON.parse(event);
    console.log(gameState)
    var playerslist = gameState["players"]

    for (playerind in playerslist) {
        var player = playerslist[playerind];
        var playerx = JSON.parse(player["x"])
        var playery = JSON.parse(player["y"])
        placeCircle(playerx, playery, 'red', 1.0)

    }
}

function placeCircle(x, y, color, size) {
    context.fillStyle = color;
    context.beginPath();
    context.arc(x * tileSize,
        y * tileSize,
        size / 10.0 * tileSize,
        0,
        2 * Math.PI);
    context.fill();
    context.strokeStyle = 'black';
    context.stroke();



}