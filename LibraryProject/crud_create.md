# CRUD - Create

## Command:
from bookshelf.models import Book

book1 = Book.objects.create(title="The Great Gatsby", author="F. Scott Fitzgerald", publication_year=1925)
print(book1)

## Output:
The Great Gatsby by F. Scott Fitzgerald (1925)
