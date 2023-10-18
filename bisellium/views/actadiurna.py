from flask import Blueprint, render_template

from bisellium.lib.api_clients.ludus import LudusAPI
from bisellium.views import api_call

bp = Blueprint("actadiurna", __name__)


@bp.route("/actadiurna")
@api_call
def all_results():
    """Serve all-results template."""
    return render_template(
        "actadiurna/all-results.html",
        duel_results=LudusAPI().get_all_duel_results(),
    )


@bp.route("/actadiurna/duels/<id>")
@api_call
def one_duel_result(id):
    """Serve one-duel-result template."""
    return render_template(
        "actadiurna/one-duel-result.html",
        duel_result=LudusAPI().get_one_duel_result(id),
    )
