# CRUD - Delete

## Command:
from bookshelf.models import Book

book = Book.objects.get(id=1)
print("Book to delete:", book)

book.delete()

all_books = Book.objects.all()
print("Remaining books:", all_books)

## Output:
Book to delete: Nineteen Eighty-Four by George Orwell (1949)
(1, {'bookshelf.Book': 1})
Remaining books: <QuerySet []>
