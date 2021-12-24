from flask import current_app

# Types for function annotations
# PEP 3107 (https://www.python.org/dev/peps/pep-3107/)
from typing import Tuple

from bisellium.models.gladiator import Gladiator
from bisellium.lib.api_clients.base import BaseAPI


class LudusAPI(BaseAPI):
    def __init__(self):
        super().__init__(
            base_url=current_app.config["LUDUS_URL"],
            status_path="/actuator/health",
        )

    def get_all_gladiators(self) -> Tuple[Gladiator]:
        """Get all gladiators."""
        return (
            Gladiator(id=r["id"], name=r["name"], type=r["type"])
            for r in self.get("/gladiators").json()
        )

    def get_one_gladiator(self, id: int) -> Gladiator:
        """Get a gladiator with full details."""
        r = self.get(f"/gladiators/{id}/full").json()
        return Gladiator(
            id=r["id"],
            name=r["name"],
            type=r["type"],
            hit_point=r["hitPoint"],
            attack=r["attack"],
            defense=r["defense"],
            equipment=r["equipment"],
        )
