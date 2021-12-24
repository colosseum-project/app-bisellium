from flask import Blueprint, render_template

bp = Blueprint("home", __name__)


@bp.route("/")
@bp.route("/home")
def index():
    """Serve home template."""
    return render_template("home/index.html")
