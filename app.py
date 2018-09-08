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
		data_type = request.form.get('datatype')
		if data_type != "tp":
			file = request.files['file']
			f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
			# add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
			file.save(f)
			return render_template("uploaded.html", user_image=f)

		if data_type == "tp":
			data = request.form.get('data')
			data = data.split("base64,")[1]
			a = base64.b64decode(data)
			b = BytesIO(a)
			im = Image.open(b)
			arr = np.array(im.getdata(), np.uint8).reshape(im.size[1], im.size[0], 3)
			send_data = pickle.dumps(arr)
			#create socket, bind, begin the sending process
			sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			sock.bind((socket.gethostname(),8000))
			sock.settimeout(2)
			i = 0
			print("Receiving...")
			while(i < 3):
				try:
					sock.sendto(send_data,('localhost',8000))  #self.ip = 'localhost'
					data,addr = sock.recvfrom(4096)
					break
				except Exception as e:
					print("Retrying...")
					i += 1
					print("Message was not received in these 2 seconds...")
					if(i == 3):
						#Error, since we have reached the max tries for retrying
						print("ERROR: MESSAGE WAS NOT RECEIVED")
						return
			print("Server replied:")
			print(data)
			sock.close()
			return render_template("result.html")

if __name__ == "__main__":
	app.run()