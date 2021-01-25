from app import app, mail
import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
from app.forms import ContactForm

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/ceremony', methods=['GET'])
def ceremony():
    return render_template('ceremony.html', title='Ceremony')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        try:
            fname = form.fname.data
            lname = form.lname.data
            text_body = form.greeting.data
            recipient = form.email.data
            msg = Message(subject="A Message from {fname} {lname}!", recipients=[recipient, 'themrs.pantsfam@gmail.com'])
            msg.body = text_body
            mail.send(msg)
            print('made it through send')
            flash('Your message has been sent!')
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            # return 'There was an issue sending your message, please try again'
    return render_template('contact.html', title='Contact', form=form)


