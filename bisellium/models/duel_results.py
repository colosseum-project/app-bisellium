import datetime

from bisellium.models.gladiator import Gladiator


class DuelResult:
    __slots__ = (
        "id",
        "timestamp",
        "first_gladiator",
        "second_gladiator",
        "winner",
        "combat_logs",
    )

    def __init__(
        self,
        id: int,
        timestamp: str,
        first_gladiator: dict,
        second_gladiator: dict,
        winner: dict,
        combat_logs: list = None,
    ):
        self.id = id
        self.timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%dT%H:%M:%S.%f%z")
        self.first_gladiator = Gladiator(
            id=first_gladiator["id"],
            name=first_gladiator["name"],
            type=first_gladiator["type"],
        )
        self.second_gladiator = Gladiator(
            id=second_gladiator["id"],
            name=second_gladiator["name"],
            type=second_gladiator["type"],
        )
        self.winner = Gladiator(
            id=winner["id"],
            name=winner["name"],
            type=winner["type"],
        )
        self.combat_logs = combat_logs

    def datestr(self):
        return self.timestamp.strftime("%Y-%m-%d")

    def timestr(self):
        return self.timestamp.strftime("%H:%M:%S")
