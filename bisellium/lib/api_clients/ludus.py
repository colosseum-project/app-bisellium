from flask import current_app

# Types for function annotations
# PEP 3107 (https://www.python.org/dev/peps/pep-3107/)
from typing import Tuple

from bisellium.models.gladiator import Gladiator
from bisellium.models.duel_results import DuelResult
from bisellium.lib.api_clients.base import BaseAPI


class LudusAPI(BaseAPI):
    def __init__(self):
        super().__init__(
            base_url=current_app.config["LUDUS_ENDPOINT"],
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

    def get_all_duel_results(self) -> Tuple[DuelResult]:
        """Get all duel results."""
        return (
            DuelResult(
                id=r["id"],
                timestamp=r["timestamp"],
                first_gladiator=r["firstGladiator"],
                second_gladiator=r["secondGladiator"],
                winner=r["winner"],
            )
            for r in self.get("/duels/results").json()
        )

    def get_one_duel_result(self, id: int) -> DuelResult:
        """Get a duel result."""
        r = self.get(f"/duels/results/{id}").json()
        return DuelResult(
            id=r["id"],
            timestamp=r["timestamp"],
            first_gladiator=r["firstGladiator"],
            second_gladiator=r["secondGladiator"],
            winner=r["winner"],
            combat_logs=r["combatLogs"],
        )
