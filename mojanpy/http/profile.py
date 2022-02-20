from typing import Dict, List, Optional, Tuple

import requests

from mojanpy.http.types.profile import DefaultProfile

from .routes import AuthenticatedRoutes
from .authentication.yggdrasil import authenticate


class MojangProfile:
    def __init__(self, access_token: Optional[str] = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__access_token = access_token
        self.__headers = {"Authorization": f"Bearer {self.__access_token}"}

    def login(self, email: str, password: str) -> None:
        self.__access_token = authenticate(email, password)["access_token"]
        return None

    def get_profile_info(self) -> Dict:

        r = requests.get(
            AuthenticatedRoutes.profile_information, headers=self.__headers
        )

        if r.status_code == 401:
            raise ValueError("Invalid token")

        data = r.json()

        return {
            "uuid": data["id"],
            "name": data["name"],
            "skin": [data["skins"][0]["url"], data["skins"][0]["variant"]],
            "capes": data["capes"],
        }
