/* variables */
var x = 0, y = 0; z = 0; rot_a = 0; rot_b = 0; rot_c = 0;

console.log("File linked");

window.addEventListener("deviceorientation", handleOrientation, true);

function handleOrientation(event) {
  console.log("Device orientation activated");
  
  var absolute = event.absolute;
  var alpha    = event.alpha;
  var beta     = event.beta;
  var gamma    = event.gamma;

  document.getElementById("orientationAbsolute").innerHTML = absolute;
  document.getElementById("orientationAlpha").innerHTML = alpha;
  document.getElementById("orientationBeta").innerHTML = beta;
  document.getElementById("orientationGamma").innerHTML = gamma;

  var obj = {absolute, alpha, beta, gamma};
  sendSock(JSON.stringify(obj));

}

var socket = new WebSocket("ws://dev.txtpen.com:5000/acc");

function sendSock(e){
 socket.send(e);
}
