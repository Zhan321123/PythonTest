"""
flask服务端
"""
from flask import Flask, render_template, url_for, redirect, request, abort

app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello World!'


@app.route('/home')
def home():
  return render_template('home.html')


@app.route('/home2/')
def home2():
  return render_template('home2.html', name='Mike', sex=1,
    hobbies=['football', 'basketball', 'swimming'])


@app.route('/test1')
def test1():
  return render_template('test1.html')


@app.route('/user/<username>')
def testString(username):
  return f'<h1 style="color:yellow; text-align:center">User {username}, Hello!</h1>'


@app.route('/blog/<int:postId>')
def TestInt(postId):
  return f'<h1>Post {postId}</h1>'


@app.route('/float/<float:number>')
def TestFloat(number):
  return f'<h1>Test [float:number], your number is {number}</h1>'


@app.route('/user/<name>')
def hello(name):
  if name == 'admin':
    return redirect(url_for('testString', username='zhan'))
  else:
    return redirect(url_for('testString', username=name))

@app.route('/post/')
def post_request():
  return render_template('post.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True, threaded=True)
