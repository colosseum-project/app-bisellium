from flask import Blueprint, render_template

from bisellium.lib.api_clients.arena import ArenaAPI
from bisellium.lib.api_clients.ludus import LudusAPI

bp = Blueprint("misc", __name__)


@bp.route("/api-status")
def api_status():
    """Serve api-status template."""
    api_services = (
        {"name": "Ludus", "status": LudusAPI().status()},
        {"name": "Arena", "status": ArenaAPI().status()},
    )
    return render_template("misc/api-status.html", api_services=api_services)


@bp.route("/glossary")
def glossary():
    """Serve glossary template."""
    return render_template("misc/glossary.html")
