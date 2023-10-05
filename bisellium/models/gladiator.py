import os

from flask import current_app
from werkzeug.utils import safe_join

from bisellium.lib.pagan import pagan

PAGAN_FOLDER_STATIC_PATH = "img/pagan"


class Gladiator:
    __slots__ = (
        "id",
        "name",
        "type",
        "hit_point",
        "attack",
        "defense",
        "equipment",
        "__pagan_filename",
    )

    def __init__(
        self,
        id: int,
        name: str,
        type: str,
        hit_point: int = None,
        attack: object = None,
        defense: object = None,
        equipment: object = None,
    ):
        self.id = id
        self.name = name.capitalize()
        self.type = type.capitalize()
        self.hit_point = hit_point
        self.attack = attack
        self.defense = defense
        self.equipment = equipment
        self.__pagan_filename = f"{name.lower()}.png"
        if not os.path.exists(self.__get_pagan_os_path()):
            self.__generate_pagan()

    def __generate_pagan(self) -> None:
        img = pagan.Avatar(self.name, pagan.SHA512)
        img.save(self.__get_pagan_folder_os_path(), self.__pagan_filename)

    def __get_pagan_folder_os_path(self) -> str:
        return safe_join(current_app.static_folder, PAGAN_FOLDER_STATIC_PATH)

    def __get_pagan_os_path(self) -> str:
        return safe_join(self.__get_pagan_folder_os_path(), self.__pagan_filename)

    def get_pagan_static_path(self) -> str:
        return f"{PAGAN_FOLDER_STATIC_PATH}/{self.__pagan_filename}"
