from app import app

# about pages
@app.route('/about')
def about():
    hero_type = 'hero'
    return render_template('about/about.html', hero_type=hero_type)