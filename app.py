from flask import Flask
from flask import render_template
from email import email

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
	return render_template("index.html")

@app.route("/register", methods=['POST', 'GET'])
def register():
	if request.method == 'POST':
		return sendEmail(request.form['email'], 'FireWatch Registration', request.form['location'])
	else:
		return render_template("register.html")
	
app.run()
