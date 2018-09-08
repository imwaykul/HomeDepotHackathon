from flask import Flask, render_template, request, json, send_from_directory
import os
import numpy as np
import base64
from PIL import Image
from io import BytesIO
import json
from ftplib import FTP 
import pickle

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def mainpage():
	return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		data = request.form.get('data')
		data = data.split("base64,")[1]
		a = base64.b64decode(data)
		b = BytesIO(a)
		im = Image.open(b)
		arr = np.array(im.getdata(), np.uint8).reshape(im.size[1], im.size[0], 3)

		#to_send = pickle.dumps(arr)
		#send the numpy array through ftp?
		#session = FTP('server.address.com','USERNAME','PASSWORD')
		#session.storbinary('STOR ', to_send)     # send the file
		#session.quit()
		return render_template("result.html")

if __name__ == "__main__":
	app.run()