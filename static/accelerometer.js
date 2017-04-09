/* variables */
var x = 0, y = 0, z = 0, rot_a = 0, rot_b = 0, rot_c = 0;
var eventTimeout;

var client_id = -1

window.addEventListener("deviceorientation", throttledHandler, true);

var socket = io.connect("ws://dev.txtpen.com:5000/sensor");
var room = io.connect("ws://dev.txtpen.com:5000/room");

var me = 'a';

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
  console.log(me);

  var absolute = event.absolute;
  var alpha    = event.alpha;
  var beta     = event.beta;
  var gamma    = event.gamma;

  document.getElementById("me").innerHTML = me;

  var obj = {absolute, alpha, beta, gamma, me};
  sendSock(obj);

}

function clickthis(){
  me = (me=='a'?'b':'a');
  document.getElementById("me").innerHTML = me;
}


function sendSock(e){
  socket.emit('push',e);
}
