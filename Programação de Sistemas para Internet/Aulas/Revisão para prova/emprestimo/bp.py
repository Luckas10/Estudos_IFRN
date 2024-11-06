from flask import Blueprint, render_template

bp_emprestimo = Blueprint(
    name='emprestimo',
    import_name=__name__,
    url_prefix='/emprestimo',
    template_folder='templates'
)


@bp_emprestimo.route('/')
def index():
    return render_template('emprestimo/index.html')