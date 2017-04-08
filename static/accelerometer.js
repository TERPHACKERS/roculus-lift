var flag = true;
var count = 0;
var x = 0, y = 0,
    vx = 0, vy = 0,
	ax = 0, ay = 0;

window.ondevicemotion = function(e) {

  var data_x = (e.accelerationIncludingGravity.x).toFixed(1);
  var data_y = (e.accelerationIncludingGravity.y).toFixed(1);
  var data_z = (e.accelerationIncludingGravity.z).toFixed(1);

  var rot_a = (e.rotationRate.alpha).toFixed(0);
  var rot_b = (e.rotationRate.beta).toFixed(0);
  var rot_c = (e.rotationRate.gamma).toFixed(0);

	document.getElementById("accelerationX").innerHTML = data_x;
	document.getElementById("accelerationY").innerHTML = data_y;
	document.getElementById("accelerationZ").innerHTML = data_z;

  document.getElementById("rotationAlpha").innerHTML = rot_a;
  document.getElementById("rotationBeta").innerHTML = rot_b;
  document.getElementById("rotationGamma").innerHTML = rot_c;

  var obj = {data_x, data_y, data_z, rot_a, rot_b, rot_c};
  sendSock(JSON.stringify(obj));

}


var socket = new WebSocket("ws://dev.txtpen.com:5000/acc");

function sendSock(e){
 socket.send(e);
}
