from flask import Flask, render_template, request, flash
from flask_wtf import Form
from wtforms import TextField, IntegerField, TextAreaField, SubmitField, RadioField, SelectField, validators, ValidationError

app = Flask(__name__)
app.secret_key = 'development key'
if __name__ == '__main__':
    app.run(debug = True)

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = ContactForm()   
    if request.method == 'POST':
        if form.validate() == False:
            flash('All fields are required.')
            return render_template('contact.html', form = form)
        else:
            return render_template('success.html')
    elif request.method == 'GET':
        return render_template('contact.html', form = form)

class ContactForm(Form):
    name = TextField("Name Of Student",[validators.Required("Please enter your name.")])
    Gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
    Address = TextAreaField("Address")  
    email = TextField("Email", [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    Age = IntegerField("age", [validators.required()])
    language = SelectField('Languages', choices = [('java', 'Java'), ('cpp', 'C++'), ('py', 'Python')])
    submit = SubmitField("Send")
