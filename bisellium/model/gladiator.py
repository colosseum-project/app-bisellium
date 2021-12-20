import os

from flask import current_app
from flask.helpers import safe_join

from bisellium.lib.pagan import pagan

PAGAN_FOLDER_STATIC_PATH = "img/pagan"


class Gladiator:
    __slots__ = ("name", "pagan_filename")

    def __init__(self, name: str):
        self.name = name.lower()
        self.pagan_filename = f"{self.name}.png"
        if not os.path.exists(self.get_pagan_os_path()):
            self.__generate_pagan()

    def __generate_pagan(self) -> None:
        img = pagan.Avatar(self.name, pagan.SHA512)
        img.save(self.__get_pagan_folder_os_path(), self.pagan_filename)

    def __get_pagan_folder_os_path(self):
        return safe_join(current_app.static_folder, PAGAN_FOLDER_STATIC_PATH)

    def get_pagan_os_path(self) -> str:
        return safe_join(self.__get_pagan_folder_os_path(), self.pagan_filename)

    def get_pagan_static_path(self) -> str:
        return f"{PAGAN_FOLDER_STATIC_PATH}/{self.pagan_filename}"
