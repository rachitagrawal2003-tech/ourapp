from flask import Blueprint, render_template

propose_day_bp = Blueprint('propose_day', __name__)

@propose_day_bp.route('/propose')
def index():
    return render_template('propose_day.html')
