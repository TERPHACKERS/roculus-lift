from flask import Flask, Blueprint, render_template
from flask_socketio import SocketIO, emit

curr_client_num = 0

html = Blueprint('html', __name__,
                 template_folder='templates')

app = Flask(__name__)
app.register_blueprint(html, url_prefix=r'/')
socketio = SocketIO(app)

@socketio.on('connect', namespace='/sensor')
def sensor_connect():

    if (curr_client_num > 1):
        disconnect()

    i = curr_client_num
    curr_client_num+=1

    print('Adding client id ',i)
    emit('set client id', {'client_id': i})

@socketio.on('disconnect', namespace='/sensor')
def sensor_disconnect():
    print('Removing client, now ',curr_client_num)

@socketio.on('push', namespace="/sensor")
def acc_socket(message):
    emit(message, broadcast=True, namespace="/vr")

@app.route('/')
def hello():
    return render_template('/index.html')

@app.route('/vr')
def render():
    return render_template('/vr.html')

if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
