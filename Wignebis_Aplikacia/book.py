# -*- coding: utf-8 -*-


from abc import ABC, abstractmethod

from errors import ValidationError


class LibraryItem(ABC):


    @abstractmethod
    def display(self) -> str:
        pass

    @abstractmethod
    def to_row(self) -> dict[str, str]:

        pass


class Book(LibraryItem):


    MIN_YEAR = 1450
    MAX_YEAR = 2100

    def __init__(self, title: str, author: str, year: int):

        self.title = title
        self.author = author
        self.year = year


    @property
    def title(self) -> str:

        return self.__title

    @title.setter
    def title(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValidationError("სათაური არ უნდა იყოს ცარიელი")

        self.__title = value.strip()

    @property
    def author(self) -> str:

        return self.__author

    @author.setter
    def author(self, value: str) -> None:
        if not isinstance(value, str) or not value.strip():
            raise ValidationError("ავტორი არ უნდა იყოს ცარიელი")
        self.__author = value.strip()

    @property
    def year(self) -> int:

        return self.__year

    @year.setter
    def year(self, value: int) -> None:

        if not isinstance(value, int) or isinstance(value, bool):
            raise ValidationError("გამოცემის წელი უნდა იყოს მთელი რიცხვი")
        if not (Book.MIN_YEAR <= value <= Book.MAX_YEAR):
            raise ValidationError(
                f"გამოცემის წელი უნდა იყოს {Book.MIN_YEAR}-დან {Book.MAX_YEAR}-მდე"
            )
        self.__year = value

    #
    def display(self) -> str:

        return (
            f"სათაური: {self.title} | "
            f"ავტორი: {self.author} | "
            f"გამოცემის წელი: {self.year}"
        )

    def to_row(self) -> dict[str, str]:

        return {
            "title": self.title,
            "author": self.author,
            "year": str(self.year),
            "kind": "book",
            "file_format": "",
        }


    def __str__(self) -> str:

        return self.display()

    def __repr__(self) -> str:

        return f"Book({self.title!r}, {self.author!r}, {self.year})"

    def __eq__(self, other: object) -> bool:

        if not isinstance(other, Book):
            return False
        return (
            self.title.lower() == other.title.lower()
            and self.author.lower() == other.author.lower()
            and self.year == other.year
        )


class EBook(Book):


    def __init__(self, title: str, author: str, year: int, file_format: str = "PDF"):
        super().__init__(title, author, year)
        if not isinstance(file_format, str) or not file_format.strip():
            raise ValidationError("ფაილის ფორმატი არ უნდა იყოს ცარიელი")
        self.file_format = file_format.strip().upper()

    def display(self) -> str:

        return f"{super().display()} | ფორმატი: {self.file_format}"

    def to_row(self) -> dict[str, str]:

        row = super().to_row()
        row["kind"] = "ebook"
        row["file_format"] = self.file_format
        return row

    def __repr__(self) -> str:
        return (
            f"EBook({self.title!r}, {self.author!r}, "
            f"{self.year}, {self.file_format!r})"
        )


def book_from_row(row: dict[str, str]) -> Book:

    year = int(row["year"])
    if row.get("kind") == "ebook":
        return EBook(row["title"], row["author"], year, row.get("file_format", "PDF"))
    return Book(row["title"], row["author"], year)
