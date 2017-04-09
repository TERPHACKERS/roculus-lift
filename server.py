from flask import Flask, Blueprint, render_template
from flask_socketio import SocketIO, emit

# client_id_set = set()
curr_client_id = 0

html = Blueprint('html', __name__,
                 template_folder='templates')

app = Flask(__name__)
app.register_blueprint(html, url_prefix=r'/')
socketio = SocketIO(app)

@socketio.on('connect', namespace='/sensor')
def sensor_connect():

    # i = 0
    # while i in client_id_set:
    #     i+=1
    # client_id_set.add(i)

    i = (curr_client_id+1)%2

    print('Adding client id ',i)
    emit('set client id', {'client_id': i})

@socketio.on('disconnect sensor', namespace='/sensor')
def sensor_disconnect(message):
    print('Removing client id ',message)
    client_id_set.remove(message)

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
