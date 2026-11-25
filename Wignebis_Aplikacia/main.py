# -*- coding: utf-8 -*-


import os
import sys

from book import Book, EBook
from book_manager import BookManager
from errors import DuplicateBookError, LibraryError


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stdin, "reconfigure"):
    sys.stdin.reconfigure(encoding="utf-8")


SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


class BookConsoleApp:
    """კონსოლის UI კლასი — BookManager-ის გარსი.

    ბიზნეს-ლოგიკა (ძებნა, წაშლა, CSV) BookManager-შია, აქ მხოლოდ
    დიალოგია მომხმარებელთან. მენეჯერი ინახება self.manager-ში,
    ამიტომ პარამეტრად აღარ გადაგვაქვს.
    """

    def __init__(self, file_path: str | None = None):
        """აპლიკაციის შექმნა და მონაცემების ჩატვირთვა."""
        self.manager = BookManager(file_path)

    @staticmethod
    def print_menu() -> None:
        """მთავარი მენიუ ეკრანზე (პროექტის მოთხოვნა 3)."""
        print()
        print("=" * 52)
        print("       წიგნების მართვის კონსოლ აპლიკაცია")
        print("=" * 52)
        print("1. ახალი წიგნის დამატება")
        print("2. ყველა წიგნის ნახვა")
        print("3. წიგნის ძებნა სათაურის მიხედვით")
        print("4. წიგნის წაშლა სათაურის მიხედვით")
        print("5. მუშაობის მაგალითი (დემო)")
        print("0. გასვლა")
        print("-" * 52)

    @staticmethod
    def read_text(prompt: str) -> str:
        """არაცარიელი ტექსტის წაკითხვა (while + ვალიდაცია)."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("⚠ ეს ველი არ უნდა იყოს ცარიელი. სცადეთ ახლიდან.")

    @staticmethod
    def read_year(prompt: str = "გამოცემის წელი: ") -> int:
        """წლის წაკითხვა int()-ით და try/except-ით."""
        while True:
            raw = input(prompt).strip()
            try:
                year = int(raw)
            except ValueError:
                print("⚠ წელი ციფრებით უნდა ჩაწეროთ (მაგ.: 1949).")
                continue
            if not (Book.MIN_YEAR <= year <= Book.MAX_YEAR):
                print(f"⚠ წელი უნდა იყოს {Book.MIN_YEAR}-დან {Book.MAX_YEAR}-მდე.")
                continue
            return year

    def add_book_flow(self) -> None:
        """წიგნის დამატების დიალოგი."""
        print("\n--- ახალი წიგნის დამატება ---")
        title = self.read_text("სათაური: ")
        author = self.read_text("ავტორი: ")
        year = self.read_year()
        try:
            book = Book(title, author, year)
            self.manager.add_book(book)
        except DuplicateBookError as error:
            print("⚠", error)
        except LibraryError as error:
            print("⚠ დამატება ვერ მოხერხდა:", error)
        else:
            print("✅ წიგნი დამატებულია და ფაილშიც შენახულია.")

    def list_books_flow(self) -> None:
        """ყველა წიგნის დეტალური სიის ჩვენება."""
        books = self.manager.list_books()
        print(f"\n--- ყველა წიგნი ({len(books)}) ---")
        if not books:
            print("სია ცარიელია. ჯერ დაამატეთ წიგნი.")
            return

        for number, book in enumerate(books, start=1):
            print(f"{number}. {book.display()}")

    def search_books_flow(self) -> None:
        """წიგნის ძებნა სათაურის მიხედვით."""
        print("\n--- წიგნის ძებნა ---")
        query = self.read_text("საძიებო სათაური (ნაწილიც შეიძლება): ")
        results = self.manager.search_by_title(query)
        if not results:
            print(f"წიგნი '{query}' ვერ მოიძებნა.")
            return
        print(f"ნაპოვნია {len(results)} წიგნი:")
        for book in results:
            print(" •", book.display())

    def delete_book_flow(self) -> None:
        """წიგნის წაშლა სათაურის მიხედვით."""
        print("\n--- წიგნის წაშლა ---")
        title = self.read_text("წასაშლელი წიგნის სათაური: ")
        if self.manager.delete_book(title):
            print("✅ წიგნი წაშლილია სიიდან და ფაილიდან.")
        else:
            print(f"⚠ წიგნი '{title}' ვერ მოიძებნა.")

    def run_demo(self) -> None:
        """მუშაობის მაგალითი — დროებითი მენეჯერი, რომ ძველს არ შეეხოს."""
        demo_path = os.path.join(SCRIPT_DIR, "demo_books.csv")
        real_manager = self.manager
        self.manager = BookManager(demo_path)
        try:
            self.manager.clear_file()

            print("\n" + "=" * 52)
            print("          მუშაობის მაგალითი (დემო)")
            print("=" * 52)

            samples = [
                Book("მასტერი და მარგარიტა", "მიხაილ ბულგაკოვი", 1967),
                Book("1984", "ჯორჯ ორუელი", 1949),
                EBook("ქართული ენის გრამატიკა", "აკადემიკოსი", 2018, "pdf"),
            ]
            print("\n1) სამი წიგნის დამატება:")
            for book in samples:
                self.manager.add_book(book)
                print("  +", book.display())

            print("\n2) ყველა წიგნის სია:")
            self.list_books_flow()

            print("\n3) ძიება '1984':")
            for book in self.manager.search_by_title("1984"):
                print("  →", book.display())
            print("\n   ძიება 'გრამატიკა':")
            for book in self.manager.search_by_title("გრამატიკა"):
                print("  →", book.display())

            print("\n4) შეცდომების დამუშავება:")
            try:
                self.manager.add_book(Book("1984", "ჯორჯ ორუელი", 1949))
            except DuplicateBookError as error:
                print("  ⚠", error)
            try:
                Book("", "უსახელო", 2020)
            except LibraryError as error:
                print("  ⚠", error)

            print("\n5) '1984'-ის წაშლა:")
            self.manager.delete_book("1984")
            print("  დარჩა:", self.manager.count, "წიგნი")
        finally:
            # finally ყოველთვის სრულდება — ნამდვილი მენეჯერი აღდგება
            self.manager = real_manager
            try:
                os.remove(demo_path)  # დროებითი ფაილის წაშლა
            except OSError as error:
                print("  ⚠ დროებითი ფაილის წაშლა ვერ მოხერხდა:", error)
            print("=" * 52)

    def run(self) -> None:
        """მთავარი ციკლი — while True და if/elif მენიუ."""
        print(f"მონაცემები: {self.manager.file_path}")

        while True:
            self.print_menu()
            choice = input("აირჩიეთ (0–5): ").strip()

            if choice == "1":
                self.add_book_flow()
            elif choice == "2":
                self.list_books_flow()
            elif choice == "3":
                self.search_books_flow()
            elif choice == "4":
                self.delete_book_flow()
            elif choice == "5":
                self.run_demo()
            elif choice == "0":
                print("გთხოვთ, კარგად იყოთ! 👋")
                break
            else:
                print("⚠ არასწორი არჩევანი. შეიყვანეთ 0-დან 5-მდე რიცხვი.")


def main() -> None:
    """შესვლის წერტილი — ობიექტის შექმნა და გაშვება."""
    app = BookConsoleApp()
    app.run()


if __name__ == "__main__":
    main()
