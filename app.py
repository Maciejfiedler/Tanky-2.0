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


@socketio.on('forward')
def handle_forward(quantity):
    if (quantity != None):
        try:
            runCommandsInSteps('forward', quantity)
        except:
            pass


def runCommandsInSteps(command, steps):
    steps = int(quantity['steps'])
    for x in range(steps):
        pass
        robot.forward(1)
        t = Timer(0.2, robot.stop)
        t.start()

def runCommand(command):
    if(command=='forward'):
        robot.forward(1)
    elif(command=='backward'):
        robot.backward(1)

    t = Timer(0.2,robot.stop)
    t.start


if '__main__' == __name__:
    socketio.run(app, host="0.0.0.0", debug=True)
