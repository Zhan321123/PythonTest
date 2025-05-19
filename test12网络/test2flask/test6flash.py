from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)

app.secret_key = '111222'

@app.route('/')
def index():
  return render_template('index6.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  error = None

  if request.method == 'POST':
    if request.form['username'] == 'admin' and request.form['password'] == '123':
      flash('You were successfully logged in')
      return redirect(url_for('index'))
    else:
      error = 'Invalid Credentials. Please try again.'

  return render_template('login6.html', error=error)


if __name__ == '__main__':
  app.run(debug=True, threaded=True, use_reloader=True,)
