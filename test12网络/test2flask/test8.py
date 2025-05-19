from flask import Flask, render_template, request, flash
from flask_wtf import FlaskForm
from wtforms import TextAreaField, IntegerField, SubmitField, RadioField, SelectField, validators

app = Flask(__name__)
app.secret_key = '123'


@app.route('/', methods=['GET', 'POST'])
def contact():
  form1 = ContactForm()

  if request.method == 'POST':
    if form1.validate():
      return 'successful'
    else:
      flash('All fields are required')
      return render_template('contact8.html', form=form1)
  elif request.method == 'GET':
    return render_template('contact8.html', form=form1)


class ContactForm(FlaskForm):
  name = TextAreaField('name of student', [validators.InputRequired('Please enter your name')])
  gender = RadioField('gender', choices=[('m', 'male'), ('f', 'female')])
  address = TextAreaField('address')
  email = TextAreaField('email',
    [validators.InputRequired('Please enter your email address'), validators.Email('please enter your email address')])
  age = IntegerField('age')
  language = SelectField('language', choices=[('py', 'python'), ('jar', 'java'), ('c', 'c++')])
  submit = SubmitField('submit')
