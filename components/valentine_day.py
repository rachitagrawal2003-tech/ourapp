from flask import Blueprint, render_template

valentine_day_bp = Blueprint('valentine_day', __name__)

@valentine_day_bp.route('/valentine')
def index():
    return render_template('valentine_day.html')
