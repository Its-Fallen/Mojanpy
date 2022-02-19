from typing import Optional, Dict

import requests

from ..routes import YggdrasilEndpoints


def authenticate(
    email: str, password: str, client_token: Optional[str] = None
) -> Dict[str, str]:
    payload = {
        "agent": {"name": "Minecraft", "version": 1},
        "username": email,
        "password": password,
        "client_token": client_token,
    }

    r = requests.post(YggdrasilEndpoints.authenticate, json=payload)

    if r.status_code == 403:
        raise ValueError("Invalid username or password")
    elif r.status_code == 410:
        raise Exception("Account was migrated to Microsoft account")

    data = r.json()

    return {"access_token": data["accessToken"], "client_token": data["clientToken"]}


def refresh(access_token: str, client_token: str) -> Dict[str, str]:
    payload = {"accessToken": access_token, "clientToken": client_token}

    r = requests.post(YggdrasilEndpoints.refresh, json=payload)

    if r.status_code == 403:
        raise ValueError("Invalid token")

    data = r.json()

    return {"access_token": data["accessToken"], "client_token": data["clientToken"]}


def validate(access_token: str, client_token: Optional[str] = None) -> bool:
    payload = {"accessToken": access_token, "clientToken": client_token}
    r = requests.post(YggdrasilEndpoints.validate, json=payload)

    if r.status_code == 204:
        return True
    else:
        return False


def signout(email: str, password: str) -> None:
    payload = {"username": email, "password": password}
    r = requests.post(YggdrasilEndpoints.signout, json=payload)

    if r.status_code == 204:
        return None
    elif r.status_code == 403:
        raise ValueError("Invalid credentials")


def invalidate(access_token: str, client_token: str) -> None:
    payload = {"accessToken": access_token, "clientToken": client_token}
    r = requests.post(YggdrasilEndpoints.invalidate, json=payload)

    if r.status_code == 204:
        return None
    elif r.status_code == 403:
        raise ValueError("Invalid token")
