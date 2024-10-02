from typing import Dict


def generate_headers() -> Dict[str, str]:
    return {"Content-Type": "application/x-www-form-urlencoded"}


def generate_payload(client_id, client_secret) -> Dict[str, str]:
    return {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
