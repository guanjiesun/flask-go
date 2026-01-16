from .import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    title = 'Home'
    user = {'username': 'Guanjie'}
    return render_template('index.html', title=title, user=user)
