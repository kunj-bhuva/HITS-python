


import datetime
from typing import Optional

class LibraryManager:
    def __init__(self, penalty_per_day: int = 2):
        self.books = {}       # book_id -> book_info
        self.members = {}     # member_id -> member_info
        self.loans = {}       # book_id -> loan_info
        self.penalty_per_day = penalty_per_day

    def add_book(self, book_id: str, title: str, author: str, genre: str):
        if book_id in self.books:
            raise ValueError("Book already exists")
        self.books[book_id] = {
            "title": title,
            "author": author,
            "genre": genre,
            "available": True
        }

    def register_member(self, member_id: str, name: str):
        if member_id in self.members:
            raise ValueError("Member already registered")
        self.members[member_id] = {
            "name": name,
            "borrowed": []
        }

    def borrow_book(self, book_id: str, member_id: str, days: int = 7):
        if book_id not in self.books:
            raise ValueError("Book not found")
        if member_id not in self.members:
            raise ValueError("Member not registered")
        if not self.books[book_id]["available"]:
            raise ValueError("Book is currently borrowed")

        due_date = datetime.date.today() + datetime.timedelta(days=days)
        self.books[book_id]["available"] = False
        self.members[member_id]["borrowed"].append(book_id)
        self.loans[book_id] = {
            "member_id": member_id,
            "due_date": due_date
        }

    def return_book(self, book_id: str, return_date: Optional[datetime.date] = None):
        if book_id not in self.loans:
            raise ValueError("Book was not borrowed")
        if return_date is None:
            return_date = datetime.date.today()

        loan = self.loans.pop(book_id)
        member_id = loan["member_id"]
        self.books[book_id]["available"] = True
        self.members[member_id]["borrowed"].remove(book_id)

        days_late = (return_date - loan["due_date"]).days
        if days_late > 0:
            penalty = days_late * self.penalty_per_day
            return {"status": "late", "days_late": days_late, "penalty": penalty}
        else:
            return {"status": "on_time"}

    def search_books(self, keyword: Optional[str] = None, genre: Optional[str] = None, available_only: bool = False):
        result = []
        for book_id, book in self.books.items():
            match = True
            if keyword and keyword.lower() not in book["title"].lower():
                match = False
            if genre and genre.lower() != book["genre"].lower():
                match = False
            if available_only and not book["available"]:
                match = False
            if match:
                result.append((book_id, book))
        return result

    def member_summary(self, member_id: str):
        if member_id not in self.members:
            raise ValueError("Member not found")
        borrowed_books = self.members[member_id]["borrowed"]
        return {
            "member_id": member_id,
            "name": self.members[member_id]["name"],
            "borrowed_books": borrowed_books
        }

# --- CLI for manual testing ---
if __name__ == "__main__":
    lib = LibraryManager()

    while True:
        print("Library Menu ---")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Search Books")
        print("6. Member Summary")
        print("0. Exit")

        choice = input("Choose an option: ")
        try:
            if choice == "1":
                bid = input("Book ID: ")
                title = input("Title: ")
                author = input("Author: ")
                genre = input("Genre: ")
                lib.add_book(bid, title, author, genre)
                print("Book added.")

            elif choice == "2":
                mid = input("Member ID: ")
                name = input("Name: ")
                lib.register_member(mid, name)
                print("Member registered.")

            elif choice == "3":
                bid = input("Book ID: ")
                mid = input("Member ID: ")
                days = int(input("Days to borrow (default 7): ") or 7)
                lib.borrow_book(bid, mid, days)
                print("Book borrowed.")

            elif choice == "4":
                bid = input("Book ID: ")
                info = lib.return_book(bid)
                print("Return info:", info)

            elif choice == "5":
                keyword = input("Keyword (press Enter to skip): ") or None
                genre = input("Genre (press Enter to skip): ") or None
                only_available = input("Only available? (y/n): ").lower() == "y"
                results = lib.search_books(keyword, genre, only_available)
                for book_id, book in results:
                    print(f"{book_id}: {book}")

            elif choice == "6":
                mid = input("Member ID: ")
                summary = lib.member_summary(mid)
                print("Summary:", summary)

            elif choice == "0":
                break
            else:
                print("Invalid option.")
        except Exception as e:
            print("Error:", e)

      