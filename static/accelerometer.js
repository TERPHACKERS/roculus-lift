/* variables */
var x = 0, y = 0, z = 0, rot_a = 0, rot_b = 0, rot_c = 0;
var eventTimeout;

var client_id = -1

window.addEventListener("deviceorientation", throttledHandler, true);

var socket = io.connect("ws://dev.txtpen.com:5000/sensor");

socket.on('connect', function () {

  socket.on('set client id', function (id) {
    client_id = id
  });

  socket.on('disconnected', function() {
    socket.emit('disconnect sensor', client_id);
  });

});

function throttledHandler(event){
  if ( !eventTimeout ) {
    eventTimeout = setTimeout(function() {
      eventTimeout = null;
      handleOrientation(event);
    }, 16.6);
  }
}

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

  var obj = {absolute, alpha, beta, gamma, client_id};
  sendSock(JSON.stringify(obj));

}

function sendSock(e){
  if(client_id!=-1){
    socket.emit('push',e);
  }
}
