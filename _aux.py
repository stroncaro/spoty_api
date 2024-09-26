from typing import Iterable

from .exceptions import InvalidJSONException


def validate_json(json: dict, *, required_fields: Iterable[str]):
    """Raise InvalidJSONException if `json` doesn't have all required fields"""
    missing_fields = (field for field in required_fields if field not in dict.keys())
    if missing_fields:
        raise InvalidJSONException("Missing keys: " + ",".join(missing_fields))
