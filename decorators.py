# -*- coding: utf-8 -*-


from functools import wraps

import requests

from models import ApiRequestError


def validate_name(func):


    @wraps(func)
    def wrapper(self, name, *args, **kwargs):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("ქალაქის სახელი არ უნდა იყოს ცარიელი.")
        return func(self, name.strip(), *args, **kwargs)

    return wrapper


def cache(func):

    saved = {}

    @wraps(func)
    def wrapper(*args, **kwargs):
        key = (args, tuple(sorted(kwargs.items())))
        if key not in saved:
            saved[key] = func(*args, **kwargs)
        return saved[key]

    return wrapper


def retry(attempts: int):


    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_error = None
            for attempt in range(1, attempts + 1):
                try:
                    return func(*args, **kwargs)
                except requests.RequestException as error:

                    last_error = error
                    print(f"  მცდელობა {attempt}/{attempts}: {error}")
            raise ApiRequestError(
                f"API მიუწვდომელია ({attempts} მცდელობის შემდეგ): {last_error}"
            )

        return wrapper

    return decorator
