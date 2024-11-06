from flask import Blueprint, redirect, url_for

bp = Blueprint(
    name = 'user',
    import_name=__name__,
    url_prefix='/user'
    )


@bp.route('/')
def index():
    return "USER_BP"


@bp.route('/register')
def register():
    return "register user"


@bp.route('/redirect')
def redirect_user():
    return redirect(url_for('book.index'))