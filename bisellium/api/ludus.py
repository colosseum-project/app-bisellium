from flask import current_app

from bisellium.api.base import BaseAPI


class LudusAPI(BaseAPI):
    def __init__(self):
        self.base_url = current_app.config["LUDUS_URL"]

    def get_all_gladiators(self):
        return self.get("gladiators")
