from test.API.controllers.books_controller import Book


class TestAPI:

    def test_get_books(self):
        books = Book()
        all_books = books.get_books()
        print(all_books)
