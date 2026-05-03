class Library:
    def __init__(self, book_name, author, available=True):
        self.book_name = book_name
        self.author = author
        self.available = available

    def checkout(self):
        if self.available:
            self.available = False
            print(f"{self.book_name} checked out.")
        else:
            print(f"{self.book_name} is not available.")

    def return_book(self):
        self.available = True
        print(f"{self.book_name} returned.")

    def display(self):
        status = "Available" if self.available else "Not Available"
        print(f"Book: {self.book_name}, Author: {self.author}, Status: {status}")


# Example usage
book1 = Library("Python Basics", "John Doe")
book1.display()
book1.checkout()
book1.display()
book1.return_book()
book1.display()