import os
import pathlib

from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

path = pathlib.Path(__file__).resolve().parent
print(path)

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join(path, './file/')  # 设置上传文件的保存路径
print(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
  return render_template('index7.html')


@app.route('/uploader', methods=['POST', 'GET'])
def upload():
  if request.method == "POST":
    file = request.files['file']
    filename = secure_filename(file.filename)
    print(filename)
    savePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(savePath)
    return 'file uploaded successfully'
  elif request.method == 'GET':
    return render_template('index7.html')


if __name__ == '__main__':
  app.run(debug=True, threaded=True, reload=True)