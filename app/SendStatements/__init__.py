from flask import Blueprint

blueprint = Blueprint(
    'SendStatements_blueprint',
    __name__,
    url_prefix='/SendStatements',
    template_folder='templates',
    static_folder='static'
)
