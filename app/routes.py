from app import app
from flask import render_template

@app.route('/')
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html', title='Home')

@app.route('/ceremony')
def ceremony():
    return "Hello, World!"

@app.route('/history')
def history():
    return "Hello, World!"

@app.route('/contact')
def contact():
    return "Hello, World!"