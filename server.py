from flask import Flask, Blueprint, render_template
from flask_socketio import SocketIO, emit

client_id_set = set()

html = Blueprint('html', __name__,
                 template_folder='templates')

app = Flask(__name__)
app.register_blueprint(html, url_prefix=r'/')
socketio = SocketIO(app)

@socketio.on('connect', namespace='/acc')
def sensor_connect():

    i = 0
    while i in client_id_set:
        i+=1

    client_id_set.add(i)

    print('Adding client id ',i)
    emit('set client id', {'client_id': i})

@socketio.on('disconnect sensor', namespace='/acc')
def sensor_disconnect(message):
    print('Removing client id ',i)
    client_id_set.remove(message)

@socketio.on('push', namespace="/acc")
def acc_socket(message):
    emit(ret, broadcast=True)

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
