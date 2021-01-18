from app import app
from flask import render_template

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/ceremony')
def ceremony():
    return render_template('ceremony.html', title='Ceremony')

@app.route('/history')
def history():
    return render_template('history.html', title='History')

@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')