from flask import Flask,render_template,redirect,request,url_for
from image import prediction
import os
app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = 'uploads/'  # Directory to save uploaded files
app.config['ALLOWED_EXTENSIONS'] = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        file = request.files['abcd']
        if file.filename == '':
            output="No selected file"
            return render_template('project2.html',out=output)
        elif file and allowed_file(file.filename):
            filename = file.filename
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            #print(f"File saved to: {file_path}")
            #print(f"File uploaded successfully! File path: {file_path}")
            output=prediction(file_path)
            return render_template('project2.html',out=output)
        else:
            output="Invalid file type"
            return render_template('project2.html',out=output)
    return render_template('project2.html')

if __name__ == '__main__':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)
