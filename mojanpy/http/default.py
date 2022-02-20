from typing import Dict, List, Optional, Union

import requests

from . import routes
from .types.profile import Profile


def get_uuid(name: str) -> Optional[str]:
    r = requests.get(routes.BaseRoutes.username_to_uuid(name))

    if r.status_code == 204:
        return None

    return r.json()["id"]


def get_uuids(names: List[str]) -> List[Dict]:
    uuids = []

    if len(names) > 10:
        raise ValueError("Max 10 names per request")

    r = requests.post(routes.BaseRoutes.usernames_to_uuids, json=names)

    for user in r.json():
        uuids.append({"name": user["name"], "uuid": user["id"]})
    return uuids


def get_name(uuid: str) -> Optional[str]:
    r = requests.get(routes.BaseRoutes.uuid_to_username(uuid))

    if r.status_code == 204:
        return None

    return r.json()["name"]


def get_name_history(uuid: str, limit: int = 20) -> List[Dict]:
    names = []

    r = requests.get(routes.BaseRoutes.name_history(uuid))

    if r.status_code == 204:
        return None

    for _, name in enumerate(list(r.json())[:limit]):
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

    if r.status_code == 204:
        return None

    return Profile(name=data["name"], uuid=data["id"], properties=data["properties"])


def get_blocked_servers(output_to_file: bool = False) -> Optional[List[str]]:
    r = requests.get(routes.BaseRoutes.blocked_servers)

    if output_to_file:
        with open("hashes.txt", "w", encoding="utf-8") as f:
            f.write(r.text)
        return None

    hashes = [server_hash.decode("utf-8") for server_hash in r.iter_lines()]

    return hashes


def get_sale_stats(options: List[str]) -> Optional[Union[List, Dict]]:
    session = requests.Session()
    sales = []
    payload = lambda options: {"metricKeys": options}

    if len(options) == 1:
        r = session.post(routes.BaseRoutes.sale_statistic, json=payload(options))
        return r.json()
    else:
        for option in options:
            r = session.post(routes.BaseRoutes.sale_statistic, json=payload([option]))
            sales.append({option: r.json()})

        return sales
