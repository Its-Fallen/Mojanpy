from typing import Dict, List

import base64
import json



class Profile:
    def __init__(self, name: str, uuid: str, properties: List, **kwargs):
        self.__name = name
        self.__uuid = uuid
        self.__properties = properties[0]
        self.__isLegacy = None


    @property
    def name(self):
        return self.__name


    @property
    def uuid(self):
        return self.__uuid


    @property
    def properties(self):
        return self.__properties


    @property
    def skin(self):
        data = json.loads(base64.b64decode(self.__properties["value"]).decode())                            
        try:
            url = data["textures"]["SKIN"]["url"]
        except:
            url = None 
        return url

    
    @property
    def cape(self):
        data = json.loads(base64.b64decode(self.__properties["value"]).decode())
        try:
            url = data["textures"]["CAPE"]["url"]
        except:
            url = None 
        return url