import flask
from flask import request
import os
import logging


app = flask.Flask(__name__)
app.config["DEBUG"] = True
logging.basicConfig(level=logging.DEBUG)

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file part', flush=True)
            return "<h1>No file part<h1>"
        file = request.files['file']
        if file.filename == '':
            print('No selected file', flush=True)
            return "<h1>No selected file<h1>"
        else:
            uploaded_path = os.path.join(os.getcwd()+file.filename)
            file.save(uploaded_path)
            read_file(uploaded_path)
            return "<h1>upload done<h1>"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
def read_file(uploaded_path):
    file1 = open(uploaded_path, 'r')
    Lines = file1.readlines()
    count = 0
    for line in Lines: 
        print("Line{}: {}".format(count, line.strip()), flush=True)

if __name__ == "__main__":
    app.run()