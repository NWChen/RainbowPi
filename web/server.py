from flask import Flask as flask
from flask import request
from flask import render_template
import leds

app = flask(__name__)

@app.route('/', methods=['POST'])
def index(name=None):
	if request.method=='POST':
		value = request.form['btn']
		print value, type(value)
		if value=='1':
			leds.fade(leds.encode(255, 0, 0))
		elif value=='2':
			leds.fade(leds.encode(0, 255, 0))
		elif value=='3':
			leds.fade(leds.encode(0, 0, 255))
	return render_template('index.html', name=name)

if __name__ == '__main__':
	app.debug = True
	app.run()