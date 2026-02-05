import os
import random
from flask import Blueprint, render_template, jsonify, current_app

rose_day_bp = Blueprint('rose_day', __name__)

def get_reasons():
    try:
        assets_dir = os.path.join(current_app.root_path, 'assets')
        reasons_path = os.path.join(assets_dir, 'reasons.txt')
        with open(reasons_path, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        return lines
    except Exception as e:
        print(f"Error reading reasons: {e}")
        return ["You are amazing!", "Your smile lights up my world."]

@rose_day_bp.route('/rose')
def index():
    return render_template('rose_day.html')

@rose_day_bp.route('/api/reasons')
def get_all_reasons():
    reasons = get_reasons()
    # Ensure we return at least 20 items if file is short, or slice to 20
    if not reasons:
        reasons = [f"Reason #{i+1}" for i in range(20)]
    return jsonify({'reasons': reasons[:20]})
