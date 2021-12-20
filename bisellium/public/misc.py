from flask import Blueprint, render_template

from bisellium import metrics

bp = Blueprint("misc", __name__)


@bp.route("/glossary")
def glossary():
    """Serve glossary template."""

    return render_template("misc/glossary.html")


# define test page
@bp.route("/test")
@metrics.do_not_track()
def test():
    return "ok"
