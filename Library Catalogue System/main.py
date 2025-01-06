class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            return True
        return False

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            return True
        return False

    def __str__(self):
        status = "Available" if not self.is_checked_out else "Checked out"
        return f"'{self.title}' by {self.author} - {status}"


class LibraryCatalogue:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def check_out_book(self, title):
        book = self.find_book(title)
        if book and book.check_out():
            return f"You have successfully checked out '{title}'."
        return f"'{title}' is not available for checkout."

    def return_book(self, title):
        book = self.find_book(title)
        if book and book.return_book():
            return f"You have successfully returned '{title}'."
        return f"'{title}' was not checked out."

    def list_books(self):
        return [str(book) for book in self.books]


# Example usage
if __name__ == "__main__":
    library = LibraryCatalogue()
    book1 = Book("1984", "George Orwell")
    book2 = Book("To Kill a Mockingbird", "Harper Lee")

    library.add_book(book1)
    library.add_book(book2)

    print(library.list_books())
    print(library.check_out_book("1984"))
    print(library.list_books())
    print(library.return_book("1984"))
    print(library.list_books())