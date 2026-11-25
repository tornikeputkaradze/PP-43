# -*- coding: utf-8 -*-


from dataclasses import dataclass
from typing import Any


class GeocodingError(Exception):
    """გეოკოდირების აპლიკაციის საერთო შეცდომა."""


class ApiRequestError(GeocodingError):
    """API-სთან დაკავშირება ვერ მოხერხდა."""


class CityNotFoundError(GeocodingError):
    """მოთხოვნილი ქალაქი API-მ ვერ იპოვა."""


@dataclass
class Location:
    """ერთი გეოგრაფიული ადგილი API-ს პასუხიდან."""

    name: str
    latitude: float
    longitude: float
    country: str = ""

    def __post_init__(self) -> None:
        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("ქალაქის სახელი არ უნდა იყოს ცარიელი.")
        self.name = self.name.strip()

        if not -90 <= self.latitude <= 90:
            raise ValueError(f"არასწორი განედი: {self.latitude}")
        if not -180 <= self.longitude <= 180:
            raise ValueError(f"არასწორი გრძედი: {self.longitude}")

    def __str__(self) -> str:
        return f"{self.name} ({self.country}): {self.latitude:.4f}, {self.longitude:.4f}"

    def to_dict(self) -> dict[str, Any]:

        return {
            "name": self.name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "country": self.country,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Location":

        try:
            return cls(
                name=data["name"],
                latitude=float(data["latitude"]),
                longitude=float(data["longitude"]),
                country=data.get("country", ""),
            )
        except (KeyError, TypeError, ValueError) as error:
            raise ValueError(f"API-ს არასწორი პასუხი: {error}") from error
