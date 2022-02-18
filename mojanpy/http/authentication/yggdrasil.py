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
