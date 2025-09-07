# CRUD - Delete

## Command:
from bookshelf.models import Book

# Fetch the book by ID
book = Book.objects.get(id=1)
print("Book to delete:", book)

# Delete the book
book.delete()

# Confirm deletion by checking all books
all_books = Book.objects.all()
print("Remaining books:", all_books)

## Output:
Book to delete: The Great Gatsby (Updated Edition) by F. Scott Fitzgerald (1925)
(1, {'bookshelf.Book': 1})
Remaining books: <QuerySet []>
