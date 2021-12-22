from flask import Flask
from flask.templating import render_template

app = Flask(__name__)

@app.route("/")
def hello_wolrd():
    return render_template("hello.html",title="Hello")
@app.route("/fisrt")
def first():
    return render_template("first.html",title="First Page")
@app.route("/second")
def second():
    return render_template("second.html",title="Second Page")

if __name__ == "__main__":
    app.run(host = "0.0.0.0")