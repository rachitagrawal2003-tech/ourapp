from flask import Blueprint, render_template

kiss_day_bp = Blueprint('kiss_day', __name__)

@kiss_day_bp.route('/kiss')
def index():
    return render_template('kiss_day.html')
