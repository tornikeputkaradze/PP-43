# -*- coding: utf-8 -*-



class LibraryError(Exception):


    pass


class ValidationError(LibraryError):


    pass


class DuplicateBookError(LibraryError):


    def __init__(self, title: str):
        self.title = title
        super().__init__(f"წიგნი ამ სათაურით უკვე არსებობს: '{title}'")


class BookNotFoundError(LibraryError):
    """მითითებული სათაურის წიგნი ვერ მოიძებნა."""

    def __init__(self, title: str):
        self.title = title
        super().__init__(f"წიგნი ვერ მოიძებნა: '{title}'")
