from flask import Blueprint, render_template

bp = Blueprint("errors", __name__)


@bp.app_errorhandler(404)
def not_found_handler(e):
    return render_template("errors/404.html"), 404


@bp.app_errorhandler(500)
def internal_server_error_handler(e):
    return render_template("errors/500.html", message=e), 500


@bp.app_errorhandler(501)
def not_implemented_handler(e):
    return render_template("errors/501.html"), 501
