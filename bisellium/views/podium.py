from flask import Blueprint, render_template

from bisellium.lib.api_clients.podium import PodiumAPI
from bisellium.views import api_call

bp = Blueprint("podium", __name__)


@bp.route("/podium")
@api_call
def gladiators():
    """Serve rank template."""
    return render_template("podium/rank.html", rank=PodiumAPI().get_rank())
