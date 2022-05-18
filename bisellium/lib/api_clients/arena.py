from flask import current_app

from bisellium.lib.api_clients.base import BaseAPI


class ArenaAPI(BaseAPI):
    def __init__(self):
        super().__init__(
            base_url=current_app.config["ARENA_URL"],
            status_path="/health",
            status_isjson=False,
        )
