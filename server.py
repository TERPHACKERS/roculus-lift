from flask import Flask, Blueprint, render_template
from flask_socketio import SocketIO, emit, disconnect
from time import time
last_received = {}

html = Blueprint('html', __name__,
                 template_folder='templates')

app = Flask(__name__)
app.register_blueprint(html, url_prefix=r'/')
socketio = SocketIO(app)

@socketio.on('connect', namespace='/sensor')
def sensor_connect():
    global curr_client_num
    check_if_expired()

    if (len(last_received.keys())>1):
        disconnect()
    else:
        i = 0
        if(i in last_received.keys()):
            i = 1

        
        print('Adding client id ',i)
        emit('set client id', {'client_id': i})

# @socketio.on('disconnect', namespace='/sensor')
# def sensor_disconnect():
#     global curr_client_num
#     print('Removing client, now ', )

@socketio.on('push', namespace="/sensor")
def acc_socket(message):
    msg = json.loads(message)
    last_received[msg['client_id']] = time()
    emit(message, broadcast=True, namespace="/vr")

@app.route('/')
def hello():
    return render_template('/index.html')

@app.route('/vr')
def render():
    return render_template('/vr.html')

def check_if_expired():
    global last_received
    for (key, value) in last_received.items():
        if time() - value > 1000:
            del last_received[key]

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
