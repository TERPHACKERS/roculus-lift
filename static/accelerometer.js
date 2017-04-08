/* variables */
var x = 0, y = 0;, z = 0, rot_a = 0; rot_b = 0; rot_c = 0;

window.ondevicemotion = function(e) {

  let x = e.accelerationIncludingGravity.x;
  let y = e.accelerationIncludingGravity.y;
  let z = e.accelerationIncludingGravity.z;

  var data_x = (x).toFixed(1);
  var data_y = (y).toFixed(1);
  var data_z = (z).toFixed(1);

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

var socket = io("ws://dev.txtpen.com:5000/acc");

function sendSock(e){
 socket.emit('push',e);
}

