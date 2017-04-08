from flask import Flask, Blueprint, render_template
from flask_sockets import Sockets

html = Blueprint('html', __name__,
                 template_folder='templates')

app = Flask(__name__)
app.register_blueprint(html, url_prefix=r'/')
sockets = Sockets(app)

@sockets.route('/acc')
def echo_socket(ws):
    while not ws.closed:
        message = ws.receive()
        print message
        ws.send(message)


@app.route('/')
def hello():
    return render_template('/index.html')


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
