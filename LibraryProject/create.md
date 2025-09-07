# CRUD - Create

## Command:
from bookshelf.models import Book

book1 = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book1)

## Output:
1984 by George Orwell (1949)
