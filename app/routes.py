from app import app, mail
from flask import render_template, flash
from app.forms import ContactForm
from flask_mail import Message

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
    fname = [form.fname.data]
    lname = [form.lname.data]
    recipient = [form.email.data, 'themrs.pantsfam@gmail.com']
    msg = Message("A Message from {fname} {lname}!", recipients=[recipient], sender='themrs.pantsfam@gmail.com')
    msg.body = ('Test Message')
    if form.validate_on_submit():
        try:
            mail.send(msg)
            flash('Your message has been sent!')
            return redirect(url_for('index'))
        except Exception as e:
            print(e)
            # return 'There was an issue sending your message, please try again'
    return render_template('contact.html', title='Contact', form=form)
