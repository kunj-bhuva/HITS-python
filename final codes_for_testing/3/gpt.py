import unittest
from c import LibraryManager
import datetime

class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        self.lib = LibraryManager()

    def test_add_book(self):
        self.lib.add_book("1", "Book1", "Author1", "Genre1")
        self.assertIn("1", self.lib.books)

    def test_register_member(self):
        self.lib.register_member("1", "Member1")
        self.assertIn("1", self.lib.members)

    def test_borrow_book(self):
        self.lib.add_book("1", "Book1", "Author1", "Genre1")
        self.lib.register_member("1", "Member1")
        self.lib.borrow_book("1", "1", 7)
        self.assertFalse(self.lib.books["1"]["available"])
        self.assertIn("1", self.lib.members["1"]["borrowed"])

    def test_return_book_on_time(self):
        self.lib.add_book("1", "Book1", "Author1", "Genre1")
        self.lib.register_member("1", "Member1")
        self.lib.borrow_book("1", "1", 7)
        return_info = self.lib.return_book("1", datetime.date.today())
        self.assertEqual(return_info["status"], "on_time")

    def test_return_book_late(self):
        self.lib.add_book("1", "Book1", "Author1", "Genre1")
        self.lib.register_member("1", "Member1")
        self.lib.borrow_book("1", "1", 7)
        return_info = self.lib.return_book("1", datetime.date.today() + datetime.timedelta(days=10))
        self.assertEqual(return_info["status"], "late")


if __name__ == '__main__':
    unittest.main()