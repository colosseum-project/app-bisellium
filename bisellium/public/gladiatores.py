from flask import Blueprint, render_template

from werkzeug.exceptions import abort

from bisellium.model.gladiator import Gladiator
from bisellium.api.ludus import LudusAPI
from bisellium.api.base import APIException

bp = Blueprint("gladiatores", __name__)


@bp.route("/gladiatores")
def index():
    """Serve Gladiatores template."""
    api = LudusAPI()

    try:
        gladiator_json = api.get_all_gladiators()
    except APIException as e:
        abort(500, e)

    gladiators = [Gladiator(g["name"]) for g in gladiator_json]

    return render_template("gladiatores/gladiatores.html", gladiators=gladiators)
