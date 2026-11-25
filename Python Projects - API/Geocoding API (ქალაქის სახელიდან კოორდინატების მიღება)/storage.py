# -*- coding: utf-8 -*-


import json
import os
from abc import ABC, abstractmethod
from typing import Any

from models import Location

DATA_DIR = "data"
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")


class HistoryStorage(ABC):


    @abstractmethod
    def load(self) -> list[Location]:
        """ჩატვირთვა."""

    @abstractmethod
    def save(self, locations: list[Location]) -> None:
        """შენახვა."""

    @abstractmethod
    def clear(self) -> None:
        """გასუფთავება."""


class JsonHistoryStorage(HistoryStorage):


    def __init__(self, path: str = HISTORY_FILE):
        self._path = path

    @property
    def path(self) -> str:
        return self._path

    def load(self) -> list[Location]:
        if not os.path.exists(self._path):
            return []
        try:
            with open(self._path, "r", encoding="utf-8") as file:
                data = json.load(file)
            return [Location.from_dict(item) for item in data]
        except (json.JSONDecodeError, ValueError, OSError) as error:

            print(f"გაფრთხილება: ისტორიის წაკითხვა ვერ მოხერხდა: {error}")
            return []

    def save(self, locations: list[Location]) -> None:
        folder = os.path.dirname(self._path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        records: list[dict[str, Any]] = [item.to_dict() for item in locations]
        with open(self._path, "w", encoding="utf-8") as file:
            json.dump(records, file, ensure_ascii=False, indent=2)

    def clear(self) -> None:
        self.save([])
