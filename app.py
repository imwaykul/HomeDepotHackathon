from flask import Flask, render_template, request, json, send_from_directory
import os

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join('static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route("/")
def mainpage():
	return render_template('main.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		file = request.files['file']
		f = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
		# add your custom code to check that the uploaded file is a valid image and not a malicious file (out-of-scope for this post)
		file.save(f)
		return render_template("uploaded.html", user_image=f)

if __name__ == "__main__":
	app.run()