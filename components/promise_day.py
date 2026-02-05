from flask import Blueprint, render_template

promise_day_bp = Blueprint('promise_day', __name__)

@promise_day_bp.route('/promise')
def index():
    return render_template('promise_day.html')
