from flask import Flask
from flask.templating import render_template
import RPi.GPIO as GPIO

app = Flask(__name__)
LED_PIN1 = 22
LED_PIN2 = 4
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN1,GPIO.OUT)
GPIO.setup(LED_PIN2,GPIO.OUT)


@app.route("/")
def hello_wolrd():
    return render_template("led2.html")
@app.route("/led/<op>")
def RED_led_op(op):
    print(op)
    if op == "on":
        GPIO.output(LED_PIN1, GPIO.HIGH)
        return "LED ON"
    elif op == "off":
        GPIO.output(LED_PIN1, GPIO.LOW)
        return "LED ON"
        
if __name__ == "__main__":
    try:
        app.run(host = "0.0.0.0")
    finally:
        GPIO.cleanup()