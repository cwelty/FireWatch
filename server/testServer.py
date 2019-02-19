from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("hello.html", name="Carson")

@app.route("/hack")
def hack():
	return "Good luck with your webserver!"
	
app.run()
