from flask import Blueprint, redirect, url_for

bp = Blueprint(
    name = 'book',
    import_name=__name__,
    url_prefix='/book'
    )


@bp.route('/')
def index():
    return "BOOK_BP"


@bp.route('/register')
def register():
    return "register book"


@bp.route('/redirect')
def redirect_user():
    return redirect(url_for('user.index'))