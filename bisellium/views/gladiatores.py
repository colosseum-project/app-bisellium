from flask import Blueprint, render_template

from bisellium.lib.api_clients.ludus import LudusAPI
from bisellium.views import api_call

bp = Blueprint("gladiatores", __name__)


@bp.route("/gladiatores")
@api_call
def all_gladiators():
    """Serve all-gladiators template."""
    return render_template(
        "gladiatores/all-gladiators.html",
        gladiators=LudusAPI().get_all_gladiators(),
    )


@bp.route("/gladiatores/<id>")
@api_call
def one_gladiator(id):
    """Serve one-gladiator template."""
    return render_template(
        "gladiatores/one-gladiator.html",
        gladiator=LudusAPI().get_one_gladiator(id),
    )
