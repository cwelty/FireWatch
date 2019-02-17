from flask import Flask
from flask import render_template
import curveinterface
from array import *

app = Flask(__name__)

@app.route("/")
def index():
#	print(request.form)
#	if request.method == 'POST':
#		sendEmail(request.form['email'], 'FireWatch Registration', request.form['location'])
	return render_template('index.html')

#@app.route("/dev")
c = [[124, 42],[123, 42],[122, 42],[121, 42],[120, 42],[124, 41],[123, 41],[122, 41],[121, 41],[120, 41],[124, 40],[123, 40],[122, 40],
[121, 40],[120, 40],[124, 39],[123, 39],[122, 39],[121, 39],[120, 39],[123, 38],[122, 38],[121, 38],[122, 37],[121, 37],[120, 37],
[119, 37],[118, 37],[121, 36],[120, 36],[119, 36],[118, 36],[117, 36],[116, 36],[121, 35],[120, 35],[119, 35],[118, 35],[117, 35],
[116, 35],[115, 35],[121, 34],[120, 34],[119, 34],[118, 34],[117, 34],[116, 34],[115, 34],[114, 34],[118, 33],[117, 33],[119, 32],
[118, 32],[117, 32],[116, 32],[115, 32]]
print(curveinterface.predict(c))

app.run()
