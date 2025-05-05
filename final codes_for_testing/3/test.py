import unittest
from c import LibraryManager
import datetime

class TestLibraryManager(unittest.TestCase):

    def setUp(self):
        self.lib = LibraryManager()

    def test_add_book_new(self):
        self.lib.add_book("123", "Harry Potter", "J.K. Rowling", "Fantasy")
        self.assertEqual(self.lib.books["123"], {'title': "Harry Potter", 'author': "J.K. Rowling", 'genre': "Fantasy", 'available': True})

    def test_add_book_existing(self):
        self.lib.add_book("456", "Lord of the Rings", "J.R.R. Tolkien", "Fantasy")
        with self.assertRaises(ValueError):
            self.lib.add_book("456", "Lord of the Rings", "J.R.R. Tolkien", "Fantasy")

    def test_add_book_empty_input(self):
        self.lib.add_book("", "", "", "")
        self.assertNotIn("", self.lib.books)

    def test_add_book_special_characters(self):
        self.lib.add_book("!@#", "The $%^& Book", "Author!@#", "Special Characters")
        self.assertEqual(self.lib.books["!#"], {'title': "The $%^& Book", 'author': "Author!@#", 'genre': "Special Characters", 'available': True})

    def test_register_member_new(self):
        self.lib.register_member("12345", "John Doe")
        self.assertIn("12345", self.lib.members)

    def test_register_member_existing(self):
        self.lib.register_member("54321", "Jane Smith")
        with self.assertRaises(ValueError):
            self.lib.register_member("54321", "Jane Smith")

    def test_register_member_special_characters(self):
        self.lib.register_member("12@3$45", "Alice")
        self.assertIn("12@3$45", self.lib.members)

    def test_register_member_empty_id(self):
        with self.assertRaises(ValueError):
            self.lib.register_member("", "Bob")

    def test_register_member_empty_name(self):
        with self.assertRaises(ValueError):
            self.lib.register_member("67890", "")

    def test_register_member_long_id(self):
        self.lib.register_member("12345678901234567890", "Charlie")
        self.assertIn("12345678901234567890", self.lib.members)

    def test_borrow_book_success(self):
        self.lib.add_book("123", "Harry Potter", "J.K. Rowling", "Fantasy")
        self.lib.register_member("456", "John Doe")
        self.lib.borrow_book("123", "456", 7)
        self.assertFalse(self.lib.books["123"]["available"])
        self.assertIn("123", self.lib.members["456"]["borrowed"])

    def test_borrow_book_invalid_days(self):
        self.lib.add_book("123", "Harry Potter", "J.K. Rowling", "Fantasy")
        self.lib.register_member("456", "John Doe")
        with self.assertRaises(ValueError):
            self.lib.borrow_book("123", "456", -1)

    def test_borrow_book_already_borrowed(self):
        self.lib.add_book("999", "Book", "Author", "Genre")
        self.lib.register_member("111", "Jane Doe")
        self.lib.borrow_book("999", "111", 7)
        with self.assertRaises(ValueError):
            self.lib.borrow_book("999", "111", 7)

    def test_return_book_on_time(self):
        self.lib.add_book("123", "Harry Potter", "J.K. Rowling", "Fantasy")
        self.lib.register_member("456", "John Doe")
        self.lib.borrow_book("123", "456", 7)
        return_info = self.lib.return_book("123", None)
        self.assertEqual(return_info, {'status': 'on_time'})

    def test_return_book_late(self):
        self.lib.add_book("456", "Book", "Author", "Genre")
        self.lib.register_member("789", "Jane Doe")
        self.lib.borrow_book("456", "789", 7)
        return_info = self.lib.return_book("456", datetime.date(2022, 5, 10))
        self.assertEqual(return_info, {'status': 'late', 'days_late': 5, 'penalty': 10})

    def test_search_books(self):
        self.lib.add_book("123", "Harry Potter", "J.K. Rowling", "Fantasy")
        self.lib.add_book("456", "Lord of the Rings", "J.R.R. Tolkien", "Fantasy")
        results = self.lib.search_books("Harry", "Fantasy", True)
        self.assertEqual(results, [("123", {'title': "Harry Potter", 'author': "J.K. Rowling", 'genre': "Fantasy", 'available': True})])

    def test_member_summary(self):
        self.lib.register_member("123", "John Doe")
        summary = self.lib.member_summary("123")
        self.assertEqual(summary, {'member_id': "123", 'name': "John Doe", 'borrowed_books': []})

if __name__ == '__main__':
    unittest.main()