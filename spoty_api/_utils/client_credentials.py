def generate_headers():
    return {"Content-Type": "application/x-www-form-urlencoded"}


def generate_payload(client_id, client_secret):
    return {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "client_secret": client_secret,
    }
