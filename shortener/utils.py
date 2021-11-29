import hashlib
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def shorten(s: str, length: int = 4) -> str:
    hash_object = hashlib.sha512(s.encode())
    hash_hex = hash_object.hexdigest()
    return hash_hex[:length]


def is_string_an_url(url_string: str) -> bool:
    validate_url = URLValidator()

    try:
        validate_url(url_string)
    except ValidationError:
        return False

    return True
