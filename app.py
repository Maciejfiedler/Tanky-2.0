from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@socketio.on('forward')
def handle_forward(quantity):
    print("forward")
    print(quantity)

if '__main__' == __name__:
    socketio.run(app, host="0.0.0.0", debug=True)