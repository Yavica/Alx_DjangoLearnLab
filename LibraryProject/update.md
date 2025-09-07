# CRUD - Update

## Command:
from bookshelf.models import Book

book = Book.objects.get(id=1)
print("Before update:", book)

book.title = "Nineteen Eighty-Four"
book.save()

updated_book = Book.objects.get(id=1)
print("After update:", updated_book)

## Output:
Before update: 1984 by George Orwell (1949)
After update: Nineteen Eighty-Four by George Orwell (1949)
