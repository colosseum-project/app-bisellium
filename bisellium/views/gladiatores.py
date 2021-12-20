from flask import Blueprint, render_template

from functools import wraps

from werkzeug.exceptions import abort

from bisellium.lib.api_clients.ludus import LudusAPI
from bisellium.lib.api_clients.exceptions import LudusAPIException

bp = Blueprint("gladiatores", __name__)


def api_call(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except LudusAPIException as e:
            abort(500, e)
        return func(*args, **kwargs)

    return wrapper_func


@bp.route("/gladiatores")
@api_call
def all_gladiators():
    """Serve all-gladiator template."""
    return render_template(
        "gladiatores/all-gladiators.html", gladiators=LudusAPI().get_all_gladiators()
    )


@bp.route("/gladiatores/<id>")
@api_call
def one_gladiator(id):
    """Serve one-gradiator template."""
    return render_template(
        "gladiatores/one-gladiator.html", gladiator=LudusAPI().get_one_gladiator(id)
    )
