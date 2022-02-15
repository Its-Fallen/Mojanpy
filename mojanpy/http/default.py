from base64 import decode
from typing import Dict, List, Optional
import json
import typing

import requests

from . import routes
from .types.profile import Profile


def get_uuid(name: str) -> Optional[str]:
    r = requests.get(routes.BaseRoutes.username_to_uuid(name))
    return r.json()["id"]


def get_uuids(names: List[str]) -> List[Dict]:
    uuids = []

    r = requests.post(routes.BaseRoutes.usernames_to_uuids, json=names)

    for user in r.json():
        uuids.append({"name": user["name"], "uuid": user["id"]})
    return uuids


def get_name_history(uuid: str, limit: int = 20) -> List[Dict]:
    names = []

    r = requests.get(routes.BaseRoutes.name_history(uuid))
    for i, name in enumerate(list(r.json())[:limit]):
        try:
            first_name_time = name["changedToAt"]
        except:
            first_name_time = None
            pass
        if first_name_time is None:
            names.append({"firstName": name["name"]})
        else:
            names.append({"name": name["name"], "changed_at": name["changedToAt"]})

    return names


def get_uuid_profile(uuid: str) -> Optional[Profile]:
    r = requests.get(routes.BaseRoutes.user_profile(uuid))
    data = r.json()

    return Profile(name=data["name"], uuid=data["id"], properties=data["properties"])


def get_blocked_servers(output_to_file: bool = True) -> Optional[List]:
    r = requests.get(routes.BaseRoutes.blocked_servers)

    if output_to_file:
        with open("hashes.txt", "w", encoding="utf-8") as f:
            f.write(r.text)
        return None

    hashes = [str(hash.decode("utf-8")) for hash in r.iter_lines()]

    return hashes
