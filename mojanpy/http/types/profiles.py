from typing import Dict, List, Optional

import base64
import json

from .default import Name, Skin, Cape

class BaseProfile:
    def __init__(
        self, 
        name: str, 
        uuid: str, 
        is_legacy: Optional[bool], 
        is_demo: Optional[bool]
    ):
        self.__name = name
        self.__uuid = uuid
        self.__is_legacy = is_legacy
        self.__is_demo = is_demo

    @property
    def name(self):
        return self.__name

    @property
    def uuid(self):
        return self.__uuid

    @property
    def is_legacy(self):
        return self.__is_legacy

    @property
    def is_demo(self):
        return self.__is_demo


class UuidProfile(BaseProfile):
    def __init__(
        self, 
        name: str, 
        uuid: str, 
        is_legacy: Optional[bool], 
        is_demo: Optional[bool],
        usernames: List[Name],
        skin: Optional[Skin],
        cape: Optional[Cape]
    ):
        super().__init__(name, uuid, is_legacy, is_demo, usernames, skin, cape)
        self.__name = name
        self.__uuid = uuid
        self.__is_legacy = is_legacy
        self.__is_demo = is_demo
        self.__usernames = usernames
        self.__skin = skin
        self.__cape = cape

    @property
    def skin(self):
        pass

    @property
    def cape(self):
        pass

    