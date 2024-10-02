from typing import List, Dict
from base64 import b64encode

import requests

from .._endpoints import AUTHORIZE


def generate_headers(client_id: str, client_secret: str) -> Dict[str, str]:
    b64_encoded_credentials = f"{client_id}:{client_secret}".encode()
    b64_encoded_credentials = b64encode(b64_encoded_credentials)
    b64_encoded_credentials = str(b64_encoded_credentials, encoding="utf-8")
    return {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Basic {b64_encoded_credentials}",
    }


def generate_payload(code: str, redirect_uri: str) -> Dict[str, str]:
    return {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
    }


def generate_authorization_url(
    client_id: str,
    redirect_uri: str,
    state: str,
    scope: List[str],
    show_dialog: bool,
) -> str:
    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,
        "response_type": "code",
        "redirect_uri": redirect_uri,
    }
    if state:
        payload["state"] = state
    if scope:
        payload["scope"] = " ".join(scope)
    if show_dialog:
        payload["show_dialog"] = "true"
    auth_page = requests.get(
        AUTHORIZE,
        params=payload,
    )
    return auth_page.url


def get_code_from_auth_redirect(auth_result: str, redirect_uri: str) -> str:
    if not auth_result.startswith(redirect_uri):
        raise ValueError(
            f"Input does not correspond with redirect_uri:\n  {redirect_uri = }\n  {auth_result  = }"
        )

    # TODO: Validate state

    auth_response_query = requests.utils.urlparse(auth_result).query
    auth_response_params = dict(q.split("=") for q in auth_response_query.split("&"))
    if "error" in auth_response_params:
        raise ValueError(f"Log in failed: {auth_response_params=}")
    code = auth_response_params["code"]
    return code
