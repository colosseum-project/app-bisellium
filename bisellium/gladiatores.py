from bisellium.classes.gladiator import Gladiator
from flask import Blueprint, render_template

bp = Blueprint("gladiatores", __name__)


@bp.route("/gladiatores")
def index():
    """Serve Gladiatores template."""

    # TODO Test values to be replaced
    names = [
        "Maxence",
        "Maxentius",
        "Clarisse",
        "Spartacus",
        "Atius",
        "Atilius",
        "Sextius",
        "Vibius",
        "Bonus",
        "Marcus",
        "Mamercus",
        "Lucus",
        "Platonus",
        "Minus",
        "Bitus",
    ]

    gladiators = [Gladiator(g) for g in names]

    return render_template("gladiatores/gladiatores.html", gladiators=gladiators)
