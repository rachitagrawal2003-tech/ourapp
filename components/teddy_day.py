from flask import Blueprint, render_template

teddy_day_bp = Blueprint('teddy_day', __name__)

@teddy_day_bp.route('/teddy')
def index():
    return render_template('teddy_day.html')
