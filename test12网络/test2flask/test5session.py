from flask import Flask, session, render_template, request, redirect, url_for

app = Flask(__name__)
app.secret_key = '111222'


@app.route('/')
def index():
  if 'name' in session and 'age' in session:
    return f'hello, {session["name"]}, you are {session["age"]} <br><a href="/logout">logout</a>'
  else:
    return 'hello, guest <br><a href="/login">login</a>'


@app.route('/login',  methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['name'] = request.form['name']
    session['age'] = request.form['age']
    return redirect(url_for('index'))
  elif request.method == 'GET':
    return render_template('post.html')


@app.route('/logout')
def logout():
  session.pop('name', None)
  session.pop('age', None)
  return redirect(url_for('index'))


if __name__ == '__main__':
  app.run(debug=True, threded=True)
