from .import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

@app.route('/about')
def about():
    return "About me: A beginner as web developer"
