from app import app

# about pages
@app.route('/')
def home():
    return "Hello world"


@app.route('/about')
def about():
    return "Hello about"