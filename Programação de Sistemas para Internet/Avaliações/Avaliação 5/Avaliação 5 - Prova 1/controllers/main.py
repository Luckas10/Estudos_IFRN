from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint(
    name='main', 
    import_name=__name__,
    url_prefix='/main'
    )

@main_bp.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)
