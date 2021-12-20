from flask import Blueprint, render_template

bp = Blueprint("misc", __name__)


@bp.route("/glossary")
def glossary():
    """Serve glossary template."""
    return render_template("misc/glossary.html")
