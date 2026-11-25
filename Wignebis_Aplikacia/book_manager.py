# -*- coding: utf-8 -*-


import csv
import os

from book import Book, book_from_row
from errors import DuplicateBookError, ValidationError


FIELDNAMES = ["title", "author", "year", "kind", "file_format"]


class BookManager:


    def __init__(self, file_path: str | None = None):

        if file_path is None:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "books.csv")
        self._file_path = file_path
        self._books: list[Book] = []
        self.load()


    @property
    def books(self) -> list[Book]:

        return list(self._books)

    @property
    def count(self) -> int:

        return len(self._books)

    @property
    def file_path(self) -> str:

        return self._file_path

    def add_book(self, book: Book) -> None:


        if any(book == existing for existing in self._books):
            raise DuplicateBookError(book.title)
        self._books.append(book)
        self.save()

    def list_books(self) -> list[Book]:

        return self.books

    def search_by_title(self, query: str) -> list[Book]:

        needle = query.strip().lower()
        if not needle:
            return []
        return [book for book in self._books if needle in book.title.lower()]

    def delete_book(self, title: str) -> bool:

        wanted = title.strip().lower()
        for index, book in enumerate(self._books):
            if book.title.lower() == wanted:
                del self._books[index]
                self.save()
                return True
        return False

    def clear_file(self) -> None:

        self._books = []
        try:
            os.remove(self._file_path)
        except FileNotFoundError:
            pass


    def save(self) -> None:

        folder = os.path.dirname(os.path.abspath(self._file_path))
        os.makedirs(folder, exist_ok=True)
        with open(self._file_path, "w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
            writer.writeheader()

            writer.writerows(book.to_row() for book in self._books)

    def load(self) -> None:

        self._books = []
        try:
            with open(self._file_path, encoding="utf-8", newline="") as file:
                reader = csv.DictReader(file)
                for line_number, row in enumerate(reader, start=2):
                    try:
                        self._books.append(book_from_row(row))
                    except (ValueError, KeyError, ValidationError) as error:

                        print(f"⚠ ხაზი {line_number} გამოტოვებულია: {error}")
        except FileNotFoundError:
            return
        except OSError as error:
            print(f"⚠ ფაილის წაკითხვა ვერ მოხერხდა: {error}")

    def __len__(self) -> int:
        return len(self._books)

    def __str__(self) -> str:

        return f"ბიბლიოთეკა: {self.count} წიგნი ({self._file_path})"
