import hashlib
import os
from pathlib import Path
from pprint import pprint

from flask_cors import CORS
import flask
from werkzeug.datastructures import FileStorage
from werkzeug.utils import secure_filename

app = flask.Flask(__name__)
CORS(app, origins='localhost')  # 只允许本机访问

app.config['JSON_AS_ASCII'] = False  # jsonify时不转为ascii
app.secret_key = '111222'  # session
app.json.ensure_ascii = False  # jsonify时返回中文
rootPath = Path(__file__).parent.resolve()  # py根目录
app.static_folder = rootPath  # 设置静态文件目录
# pprint(app.config)
app.config['UPLOAD_FOLDER'] = rootPath / 'file'  # 文件上传目录
app.template_folder = rootPath / 'file'  # 模板目录
app.logger.setLevel('DEBUG')  # 日志等级为最低


@app.route('/api/province', methods=['GET'])
def getProvince():
  return flask.jsonify({
    'message': "获取成功",
    'province': ['北京', '浙江', '广东']
  })


@app.route('/api/city', methods=['GET'])
def getCity():
  province = flask.request.args.get('province')
  app.logger.warning(province)
  if province == '北京':
    result = {province: ['天安门', '故宫']}
  elif province == '浙江':
    result = {province: ['杭州', '宁波']}
  elif province == '广东':
    result = {province: ['广州', '深圳']}
  else:
    result = {'message': '没有这个省份'}
  if result.get('message') is not None:
    result['message'] = '获取成功'
  return flask.jsonify(result)


@app.route('/api/area', methods=['GET'])
def getArea():
  province = flask.request.args.get('province')
  city = flask.request.args.get('city')
  if province == '浙江' and city == '杭州':
    return flask.jsonify({'message': "获取成功", 'area': ['美食荒漠', '没了']})
  else:
    return flask.jsonify({'message': "总比去杭州强"})


@app.route('/api/news', methods=['GET'])
def getNews():
  return flask.jsonify({'message': "获取新闻成功",
                        "news": [
                          {"id": 0, "title": "新闻1", "content": "新闻内容1"},
                          {"id": 1, "title": "新闻2", "content": "新闻内容2"},
                          {"id": 2, "title": "新闻3", "content": "新闻内容3"},
                          {"id": 3, "title": "新闻4", "content": "新闻内容4"},
                        ]
                        })


users = {
  'admin': '123456',
  'zhan': '666666'
}


@app.route('/api/register', methods=['POST'])
def register():
  username = flask.request.json.get('username')
  password = flask.request.json.get('password')
  result = {'data': None}
  if username in users.keys():
    result['message'] = '用户已存在'
    result['code'] = 10005
  elif (6 < len(username) < 16) or (6 < len(password) < 16):
    result['message'] = '用户名或密码长度范围[6, 16]'
    result['code'] = 10002
  else:
    users[username] = password
    result['message'] = '注册成功'
    result['code'] = 10000
    result['data'] = {"username": username}
  return flask.jsonify(result)


@app.route('/api/login', methods=['POST'])
def login():
  auth = flask.request.authorization
  if not auth or not auth.username or not auth.password:
    return flask.jsonify({'message': '未输入输入用户名和密码'})
  username, password = auth.username, auth.password
  result = {'data': None}
  if username in users.keys():
    if users[username] == password:
      result['message'] = '登录成功'
      result['code'] = 10000
    else:
      result['message'] = '密码错误'
      result['code'] = 10001
  else:
    result['message'] = '用户不存在'
    result['code'] = 10004
    result['data'] = {'username': username}
  return flask.jsonify(result)


books = [
  {"pid": 0, "title": "书1", "author": "作者1", "price": 10},
  {"pid": 1, "title": "书2", "author": "作者2", "price": 20},
  {"pid": 2, "title": "书3", "author": "作者3", "price": 30},
  {"pid": 3, "title": "书4", "author": "作者4", "price": 400},
]
pids = 4


@app.route('/api/books', methods=['GET', 'POST', 'DELETE'])
def getBooks():
  if flask.request.method == 'GET':
    return flask.jsonify({
      'message': "获取成功",
      "books": books
    })
  elif flask.request.method == 'POST':
    global pids
    book = flask.request.json
    if book.get('title') is None or book.get('author') is None or book.get('price') is None:
      return flask.jsonify({'message': '添加失败', 'code': 10001})
    book['pid'] = pids
    pids += 1
    books.append(book)
  elif flask.request.method == 'DELETE':
    pid = flask.request.json.get('pid')
    for i in range(len(books)):
      if books[i]['pid'] == pid:
        del books[i]
        return flask.jsonify({'message': '删除成功', 'code': 10000})
  else:
    flask.abort(404)


@app.route('/api/book/<int:pid>', methods=['GET', 'PUT'])
def getBook(pid):
  if flask.request.method == 'GET':
    for book in books:
      if book['pid'] == pid:
        return flask.jsonify({'message': '获取成功', 'code': 10000, 'book': book})
  elif flask.request.method == 'PUT':
    book = flask.request.json
    for i in range(len(books)):
      if books[i]['pid'] == pid:
        books[i] = book
        return flask.jsonify({'message': '修改成功', 'code': 10000})
    else:
      return flask.jsonify({'message': '未找到该图书', 'code': 10001})
  else:
    flask.abort(404)


def logFile(file: FileStorage):
  app.logger.info({
    'filename': file.filename,
    'name': file.name,
    'contentType': file.content_type,
    'contentLength': file.content_length,
    'mimetype': file.mimetype,
    'mimetypeParams': file.mimetype_params,
    'headers': file.headers,
    'stream': file.stream,
  })


@app.route('/api/avatar', methods=['POST', 'GET', 'Delete'])
def avatar():
  if flask.request.method == 'POST':
    if 'file' not in flask.request.files:
      return flask.jsonify({'message': '上传失败，未指定file参数', 'code': 10001})
    file = flask.request.files.get('file')
    filename = secure_filename(file.filename)
    if '.' not in filename or filename.rsplit('.', 1)[1].lower() not in ['svg', 'png', 'jpg', 'jpeg']:
      return flask.jsonify({'message': '上传失败，文件类型错误', 'code': 10002})
    if file.content_length > 2 * 1024 * 1024:
      return flask.jsonify({'message': '上传失败，文件超过2mb', 'code': 10003})
    savePath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    if os.path.exists(savePath):
      return flask.jsonify({'message': '上传失败，文件已存在', 'code': 10004})
    file.save(savePath)
    return flask.jsonify({'message': '上传成功', 'code': 10000})

  elif flask.request.method == "GET":
    if 'filename' not in flask.request.args:
      return flask.jsonify({'message': '获取失败，未指定filename参数', 'code': 10001})
    filename = flask.request.args.get('filename')
    if not os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
      return flask.jsonify({'message': '获取失败，未找到该文件', 'code': 10002})
    return flask.send_from_directory(app.config['UPLOAD_FOLDER'], filename)

  elif flask.request.method == "DELETE":
    filename = flask.request.args.get('filename')
    os.remove(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    return flask.jsonify({'message': '删除成功', 'code': 10000})
  else:
    flask.abort(404)


@app.route('/api/article', methods=['POST', 'GET'])
def article():
  if flask.request.method == "POST":
    files = flask.request.files.getlist('files')
    if len(files) == 0:
      return flask.jsonify({'message': '请上传文件', 'code': 10001})
    for file in files:
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], file.filename))
    return flask.jsonify({'message': '上传成功', 'code': 10000})
  elif flask.request.method == "GET":
    filename = flask.request.args.get('filename')
    return flask.send_from_directory(app.config['UPLOAD_FOLDER'], filename)
  else:
    flask.abort(404)


@app.errorhandler(404)
def to404(error):
  app.logger.error(error)
  return flask.render_template('404.html')


@app.route('/')
def index():
  return flask.redirect(flask.url_for('home'))


@app.route('/home')
def home():
  return flask.jsonify({'message': """Welcome to zhan's interface!"""})


if __name__ == '__main__':
  app.run(debug=True, host='127.0.0.1', port=5000)
