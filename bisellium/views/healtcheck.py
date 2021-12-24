from flask import Blueprint

from bisellium.extensions import metrics

bp = Blueprint("healtcheck", __name__)


@bp.route("/healthcheck")
@bp.route("/status")
@metrics.do_not_track()
def healthcheck():
    """Serve healthcheck/status page."""
    return "up"
