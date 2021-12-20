from functools import wraps
from flask import current_app


from bisellium.models.gladiator import Gladiator
from bisellium.lib.api_clients.base import BaseAPI
from bisellium.lib.api_clients.exceptions import APIException, LudusAPIException


def call(func):
    @wraps(func)
    def wrapper_func(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except APIException as e:
            raise LudusAPIException(
                f"Cannot get gladiators from the Ludus. reason: {e}"
            )
        return func(*args, **kwargs)

    return wrapper_func


class LudusAPI(BaseAPI):
    def __init__(self):
        self.base_url = current_app.config["LUDUS_URL"]

    @call
    def get_all_gladiators(self):
        return [
            Gladiator(g["id"], g["name"], g["type"])
            for g in self.get("gladiators").json()
        ]

    @call
    def get_one_gladiator(self, id):
        r = self.get(f"gladiators/{id}/full").json()
        return Gladiator(
            r["id"], r["name"], r["type"], r["ability"], r["weapon"], r["armour"]
        )
