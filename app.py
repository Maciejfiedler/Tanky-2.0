from flask import Flask, render_template
from gpiozero import Robot

app = Flask(__name__)
robot = Robot(left=(7,8),right=(9,10))

@app.route("/")
def index():
    return render_template("index.html")

@app.context_processor
def drive_forward():
    print("forward")
    robot.backward(1)
    return dict(forward_func="console.log('fordward')")