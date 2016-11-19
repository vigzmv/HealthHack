from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os
from pdf import read_liver_pdf
from body_models import model_liver
clf = model_liver()

UPLOAD_FOLDER = os.getcwd()
ALLOWED_EXTENSIONS = set(['pdf'])
template_dir = os.getcwd()+'/docs/'

app = Flask(__name__, template_folder=template_dir,static_folder="docs")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/',methods = ['GET','POST'])
def index():
	if request.method == "GET":
		return render_template('index.html')
	if request.method ==  "POST":
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		filename = secure_filename(file.filename)
		file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		path = os.path.join(app.config['UPLOAD_FOLDER'])
		try:
			c = read_liver_pdf(path, file.filename)
			os.remove('lft.pdf')
			return str(clf.predict(c)[0])
		except Exception as e:
			return str(e)
		return request.form['firstname']






if __name__=='__main__':
	app.run(debug=True)
