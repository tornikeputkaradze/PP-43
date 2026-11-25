# -*- coding: utf-8 -*-


import requests

from decorators import cache, retry, validate_name
from models import CityNotFoundError, Location

BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "geocoding-console-app/1.0",
}
TIMEOUT = 5


class GeocodingClient:
    """კლიენტი, რომელიც ქალაქის სახელიდან კოორდინატებს იღებს."""

    def __init__(self, base_url: str = BASE_URL, timeout: int = TIMEOUT):
        self._base_url = base_url          # encapsulation: ველი პრივატულია
        self._timeout = timeout

    @property
    def base_url(self) -> str:
        return self._base_url

    @validate_name
    @cache
    @retry(attempts=3)
    def search(self, name: str, count: int = 1, language: str = "ka") -> list[Location]:

        params = {"name": name, "count": count, "language": language}

        response = requests.get(
            self._base_url,
            params=params,
            headers=HEADERS,
            timeout=self._timeout,
        )
        response.raise_for_status()
        data = response.json()

        results = data.get("results", [])
        if not results:
            raise CityNotFoundError(f'ქალაქი "{name}" ვერ მოიძებნა.')

        return [Location.from_dict(item) for item in results]
