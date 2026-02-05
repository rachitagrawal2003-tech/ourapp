from flask import Blueprint, render_template

hug_day_bp = Blueprint('hug_day', __name__)

@hug_day_bp.route('/hug')
def index():
    return render_template('hug_day.html')
