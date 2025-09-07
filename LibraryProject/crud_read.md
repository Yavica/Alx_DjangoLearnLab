# CRUD - Read

## Command:
from bookshelf.models import Book

# Get all books
books = Book.objects.all()
print(books)

# Get a single book by ID
book = Book.objects.get(id=1)
print(book)

## Output:
<QuerySet [<Book: The Great Gatsby by F. Scott Fitzgerald (1925)>]>
The Great Gatsby by F. Scott Fitzgerald (1925)
