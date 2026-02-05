from flask import Blueprint, render_template

chocolate_day_bp = Blueprint('chocolate_day', __name__)

@chocolate_day_bp.route('/chocolate')
def index():
    return render_template('chocolate_day.html')
