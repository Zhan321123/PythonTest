from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index6.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None

  if request.method == 'POST':
    if request.form['name']!='admin' or request.form['password']!='123':
      error = 'Invalid Credentials. Please try again.'
