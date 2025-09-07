# CRUD - Update

## Command:
from bookshelf.models import Book

# Fetch the book by ID
book = Book.objects.get(id=1)
print("Before update:", book)

# Update the book's title
book.title = "The Great Gatsby (Updated Edition)"
book.save()

# Fetch again to confirm update
updated_book = Book.objects.get(id=1)
print("After update:", updated_book)

## Output:
Before update: The Great Gatsby by F. Scott Fitzgerald (1925)
After update: The Great Gatsby (Updated Edition) by F. Scott Fitzgerald (1925)
