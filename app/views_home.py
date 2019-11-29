from app import app

from flask import render_template

# home pages
@app.route('/')
def home():
    hero_type = 'hero'
    return render_template('home/home.html', hero_type=hero_type)

@app.route('/engaging-with-flask')
def engaging_with_flask():
    hero_type = 'hero-advert'
    return render_template('home/engaging-with-flask.html', hero_type=hero_type)

@app.route('/switching-between-photos')
def switching_between_photos():
    hero_type = 'hero-advert'
    title = "Switching Between Photos"
    return render_template('home/switching-between-photos.html',
                                hero_type=hero_type,
                                title=title)

# misc pages
@app.route('/todo')
def todo():
    hero_type = 'hero'
    return render_template('todo.html', hero_type=hero_type)

@app.errorhandler(404)
def page_not_found(error):
    return 'You took a wrong turn. Go back.', 404