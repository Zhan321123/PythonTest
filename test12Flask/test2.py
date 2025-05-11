from flask import Flask, render_template, url_for, redirect, request
from markupsafe import escape
app = Flask(__name__)


@app.route('/')
def index():
  return 'Hello World!'

@app.route('/<name>')
def hello(name):
  return f'<h1 style="color:yellow; text-align:center">User {escape(name)}, Hello!</h1>'

if __name__ == '__main__':
  app.run(debug=True, port=5000, host='127.0.0.1', use_reloader=True, threaded=True)
