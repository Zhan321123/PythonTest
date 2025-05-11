from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def index():
  return 'Hello'

@app.route('/set')
def setCookie():
  resp = make_response("设置cookie")
  resp.set_cookie('test_key','test_value', max_age=3600)
  return resp

@app.route('/get')
def getCookie():
  cookie = request.cookies.get('test_key')
  return cookie

@app.route('/delete')
def deleteCookie():
  resp = make_response("删除cookie")
  resp.delete_cookie('test_key')
  return resp

if __name__ == '__main__':
    app.run(debug=True)