from bookshelf.models import Book

# Fetch the book by ID
book = Book.objects.get(id=1)
print("Book to delete:", book)

# Delete the book
book.delete()

# Confirm deletion by checking all books
all_books = Book.objects.all()
print("Remaining books:", all_books)
