import hashlib
from pprint import pprint

import flask

app = flask.Flask(__name__)

app.config['JSON_AS_ASCII'] = False  # jsonify时不转为ascii
app.secret_key = '111222'


@app.route('/api/province', methods=['GET'])
def getProvince():
  return flask.jsonify({
    'message': "获取成功",
    'province': ['北京', '浙江', '广东']
  })


@app.route('/api/city', methods=['GET'])
def getCity():
  province = flask.request.args.get('city')
  # app.logger.warning(province)
  if province == '北京':
    result = {province: ['天安门', '故宫']}
  elif province == '浙江':
    result = {province: ['杭州', '宁波']}
  elif province == '广东':
    result = {province: ['广州', '深圳']}
  else:
    result = {'message': '没有这个省份'}
  if result.get('message'):
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


def generateUid(username, password, salt='zhan is god'):
  return hashlib.sha256((username + password + salt).encode()).hexdigest()[:6]


users = {
  'admin': {'password': '123456', 'uid': generateUid('admin', '123456')}
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
    uid = generateUid(username, password)
    users[username] = {'password': password, 'uid': uid}
    result['message'] = '注册成功'
    result['code'] = 10000
    result['data'] = {"uid": uid, "username": username}
  return flask.jsonify(result)


@app.route('/api/login', methods=['POST'])
def login():
  username = flask.request.json.get('username')
  password = flask.request.json.get('password')
  result = {'data': None}
  if username in users.keys():
    if users[username]['password'] == password:
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


if __name__ == '__main__':
  app.run(debug=True)
