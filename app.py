import os
from flask import Flask, render_template, send_from_directory, Blueprint

app = Flask(__name__)
app.config['SECRET_KEY'] = 'valentine_secret_key'

# Configuration for Assets
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'assets')

@app.route('/assets/<path:filename>')
def custom_static(filename):
    return send_from_directory(ASSETS_DIR, filename)

# Main Dashboard Route
@app.route('/')
def index():
    days = [
        {"id": "rose", "date": "Feb 7", "title": "Rose Day", "icon": "fa-rose", "color": "text-red-500", "link": "/rose"},
        {"id": "propose", "date": "Feb 8", "title": "Propose Day", "icon": "fa-ring", "color": "text-yellow-500", "link": "/propose"},
        {"id": "chocolate", "date": "Feb 9", "title": "Chocolate Day", "icon": "fa-cookie-bite", "color": "text-amber-700", "link": "/chocolate"},
        {"id": "teddy", "date": "Feb 10", "title": "Teddy Day", "icon": "fa-paw", "color": "text-brown-500", "link": "/teddy"},
        {"id": "promise", "date": "Feb 11", "title": "Promise Day", "icon": "fa-hand-holding-heart", "color": "text-blue-500", "link": "/promise"},
        {"id": "hug", "date": "Feb 12", "title": "Hug Day", "icon": "fa-people-arrows", "color": "text-pink-500", "link": "/hug"},
        {"id": "kiss", "date": "Feb 13", "title": "Kiss Day", "icon": "fa-kiss-wink-heart", "color": "text-red-600", "link": "/kiss"},
        {"id": "valentine", "date": "Feb 14", "title": "Valentine's Day", "icon": "fa-heart", "color": "text-red-600", "link": "/valentine"},
    ]
    return render_template('index.html', days=days)

from components.rose_day import rose_day_bp
from components.propose_day import propose_day_bp
from components.chocolate_day import chocolate_day_bp
from components.teddy_day import teddy_day_bp
from components.promise_day import promise_day_bp
from components.hug_day import hug_day_bp
from components.kiss_day import kiss_day_bp
from components.valentine_day import valentine_day_bp

app.register_blueprint(rose_day_bp)
app.register_blueprint(propose_day_bp)
app.register_blueprint(chocolate_day_bp)
app.register_blueprint(teddy_day_bp)
app.register_blueprint(promise_day_bp)
app.register_blueprint(hug_day_bp)
app.register_blueprint(kiss_day_bp)
app.register_blueprint(valentine_day_bp)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
