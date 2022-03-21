from flask import Blueprint, render_template

from functools import wraps

from werkzeug.exceptions import abort

from bisellium.lib.api_clients.ludus import LudusAPI
from bisellium.lib.api_clients.exceptions import APIEndpointException

bp = Blueprint("actadiurna", __name__)


def api_call(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except APIEndpointException as e:
            abort(500, e)
        return func(*args, **kwargs)

    return wrapper_func


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
