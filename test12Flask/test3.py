from flask import Flask, request, abort, redirect, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('post.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
      if request.form['name'] == 'admin':
        return redirect(url_for('success'))
      if int(request.form['age']) > 18:
        return redirect(url_for('success'))
      else:
        abort(401)
    elif request.method == "GET":
      return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'Success'

if __name__ == '__main__':
    app.run(debug=True, threaded=True)