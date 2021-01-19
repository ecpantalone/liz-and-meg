from app import app
from flask import render_template, flash

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/ceremony')
def ceremony():
    return render_template('ceremony.html', title='Ceremony')

@app.route('/contact')
def contact():
    recipient = [form.email.data, 'themrs.pantsfam@gmail.com']
    msg = Message("A Message to Liz & Meg", recipients=[recipient], sender=form.email.data)
    msg.body = form.message.data
    try:
        mail.send(msg)
        flash('Your message has been sent!')
        return redirect(url_for('index'))
    except:
        return 'There was an issue sending your message, please try again'
    return render_template('contact.html', title='Contact', form=form)