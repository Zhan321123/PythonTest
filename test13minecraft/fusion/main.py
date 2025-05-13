import base64
import io
import os.path
import webbrowser
from pathlib import Path
from utils import *
from flask import Flask, request, send_file, render_template

app = Flask(__name__)

rootPath = Path(__file__).parent.resolve()
app.template_folder = rootPath
app.static_folder = rootPath
filePath = os.path.join(rootPath, './file/')


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/lib/<jsLibrary>')
def getLib(jsLibrary):
  jsFile = os.path.join(filePath, jsLibrary)

  if not os.path.isfile(jsFile):
    return "文件不存在", 404

  try:
    mtime = os.path.getmtime(jsFile)
    # 计算ETag (基于文件修改时间和大小)
    file_size = os.path.getsize(jsFile)
    etag = f'"{mtime}-{file_size}"'
    # 获取请求中的If-None-Match头
    client_etag = request.headers.get('If-None-Match')
    # 比较ETag
    if client_etag == etag:
      return '', 304
    # 设置响应头
    response = send_file(jsFile, mimetype='text/javascript')
    response.headers['Cache-Control'] = 'public, max-age=315360'
    response.headers['ETag'] = etag
    return response
  except Exception as e:
    return f"后端出现异常: {str(e)}", 500


@app.route('/favicon.svg')
def favicon():
  f = os.path.join(filePath, 'logo.svg')
  return send_file(f, mimetype='image/svg+xml')


@app.route('/api/generate', methods=['POST'])
def generate():
  fileUrl = request.form['file']
  mode = request.form['mode']
  pad = request.form['pad']
  mime_type, encoded_data = fileUrl.split(',', 1)
  decoded_data = base64.b64decode(encoded_data)
  buffer = io.BytesIO(decoded_data)
  img = Image.open(buffer)
  pixels = getPixelData(img)
  out = generateFusion(pixels, int(pad), mode)
  resultImg = drawPixel(out)
  resultImg.convert('P')
  pngBuffer = io.BytesIO()
  resultImg.save(pngBuffer, format='png')
  pngBuffer.seek(0)
  return send_file(pngBuffer, mimetype='image/png', as_attachment=False)

if __name__ == '__main__':
  app.run(host='127.0.0.1')
  webbrowser.open(f'http://127.0.0.1:{app.config["PORT"]}')
