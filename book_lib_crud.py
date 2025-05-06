class Book:
    """Model class representing a Book."""
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book[ID: {self.book_id}, Title: '{self.title}', Author: {self.author}]"


class Library:
    """CRUD operations for managing books using a list."""
    def __init__(self):
        self.books = []

    def create_book(self):
        """Add a new book to the library."""
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Book Title: ")
        author = input("Enter Author Name: ")
        new_book = Book(book_id, title, author)
        self.books.append(new_book)
        print(f"Book added successfully: {new_book}\n")

    def read_books(self):
        """Display all books."""
        if not self.books:
            print("No books available in the library.\n")
        else:
            print("\nList of Books:")
            for book in self.books:
                print(book)
            print()

    def update_book(self):
        """Update book details."""
        book_id = int(input("Enter Book ID to update: "))
        for book in self.books:
            if book.book_id == book_id:
                new_title = input("Enter new title (press Enter to skip): ")
                new_author = input("Enter new author (press Enter to skip): ")
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                print(f"Book updated successfully: {book}\n")
                return
        print("Book not found!\n")

    def delete_book(self):
        """Delete a book by ID."""
        book_id = int(input("Enter Book ID to delete: "))
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book deleted successfully: {book}\n")
                return
        print("Book not found!\n")


# **Menu-Driven Interface**
def main():
    library = Library()
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            library.create_book()
        elif choice == "2":
            library.read_books()
        elif choice == "3":
            library.update_book()
        elif choice == "4":
            library.delete_book()
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")


# **Run the Program**
if __name__ == "__main__":
    main()
