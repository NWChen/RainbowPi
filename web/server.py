from flask import Flask as flask
from flask import request
from flask import render_template

app = flask(__name__)

@app.route('/', methods=['POST'])
def index(name=None):
	if request.method=='POST':
		value = request.form['btn']
		print value
	return render_template('index.html', name=name)

if __name__ == '__main__':
	app.debug = True
	app.run()