from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Timer
from gpiozero import Robot

app = Flask(__name__)
socketio = SocketIO(app)
robot = Robot(left=(7,8), right=(9,10))


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on('message')
def handle_message(command):
    runCommand(command)

def runCommand(command):
    if(command=='forward'):
        print("driving forward")
        robot.forward(1)

    elif(command=='backward'):
        print("driving backwards")
        robot.backward(1)

    elif(command=='right'):
        print("driving right")
        robot.right(1)
        
    elif(command=='left'):
        print("driving left")
        robot.left(1)
    else:
        print("error")

    t = Timer(0.25, robot.stop)
    t.start()



if '__main__' == __name__:
    socketio.run(app, host="0.0.0.0", debug=False)
