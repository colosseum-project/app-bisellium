from flask import Blueprint, render_template

from functools import wraps

from werkzeug.exceptions import abort

from bisellium.lib.api_clients.podium import PodiumAPI
from bisellium.lib.api_clients.exceptions import APIEndpointException

bp = Blueprint("podium", __name__)


def api_call(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except APIEndpointException as e:
            abort(500, e)
        return func(*args, **kwargs)

    return wrapper_func


@bp.route("/podium")
@api_call
def gladiators():
    """Serve rank template."""
    return render_template("podium/rank.html", rank=PodiumAPI().get_rank())
