from flask import current_app

# Types for function annotations
# PEP 3107 (https://www.python.org/dev/peps/pep-3107/)
from typing import Any

from bisellium.lib.api_clients.base import BaseAPI


class PodiumAPI(BaseAPI):
    def __init__(self):
        super().__init__(
            base_url=current_app.config["PODIUM_ENDPOINT"],
            status_path="/health",
            status_isjson=False,
        )

    def get_rank(self) -> Any:
        """Get all gladiators."""
        return self.get("/rank").json()
