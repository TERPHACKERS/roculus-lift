from flask import Flask, Blueprint, render_template
from flask_socketio import SocketIO, emit, disconnect, join_room, leave_room ,send
import json

html = Blueprint('html', __name__,
                 template_folder='templates')

app = Flask(__name__)
app.register_blueprint(html, url_prefix=r'/')
socketio = SocketIO(app)
################################# WS

@socketio.on('push', namespace="/sensor")
def acc_socket(message):
    emit(message, broadcast=True)

a = False
b = False

@socketio.on('join', namespace='/room')
def on_join():
    global a,b
    print 'join'
    if a and b:
        return
    join_room('default')
    me = 'a'
    if a:
        me = 'b'

    print me
    if me == 'b':
        b = True
    else:
        a = True
    emit('+'+me, room="default")

@socketio.on('leave', namespace='/room')
def on_leave():
    me = data['me']
    leave_room('default')
    send('-'+me, room="default")

################################ app

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
