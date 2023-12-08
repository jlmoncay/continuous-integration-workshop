import unittest
from unittest.mock import patch
from libraryBookCS import Library

class TestLibraryBookCheckoutSystem(unittest.TestCase):

    @patch('builtins.input', side_effect=['1', 'Book1', '2', 'done'])
    def test_checkout_books(self, mock_input):
        library = Library()
        library.checkout_books()

        # Add more assertions based on your application's behavior
        # For example, check if the checkout summary is displayed correctly.

    @patch('builtins.input', side_effect=['Book1', '2', 'done'])
    def test_return_books(self, mock_input):
        library = Library()
        library.checked_out_books = [{"book": library.books[0], "quantity": 2}]

        library.return_books()

        # Add more assertions based on your application's behavior
        # For example, check if the return summary is displayed correctly.

if __name__ == '__main__':
    unittest.main()
