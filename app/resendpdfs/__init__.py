from flask import Blueprint

blueprint = Blueprint(
    'resendpdfs_blueprint',
    __name__,
    url_prefix='/resendpdfs',
    template_folder='templates',
    static_folder='static'
)
