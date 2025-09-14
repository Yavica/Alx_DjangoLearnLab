import os
import django

# Setup Django so this script works when run directly with "python3 -m"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

# Now import models AFTER Django setup
from relationship_app.models import Author, Book, Library, Librarian

# Create an author (avoid duplicates)
author1, _ = Author.objects.get_or_create(name="Author One")

# Create a library (avoid duplicates)
library1, _ = Library.objects.get_or_create(
    name="Central Library",
    defaults={"location": "Downtown"}
)

# Create a librarian (avoid duplicates)
librarian1, _ = Librarian.objects.get_or_create(name="John Doe", library=library1)

# Create a book (avoid duplicates)
book1, _ = Book.objects.get_or_create(
    title="Django for Beginners",
    author=author1,
    library=library1
)

# Print results to confirm
print("Author:", author1.name)
print("Library:", library1.name, "-", library1.location)
print("Librarian:", librarian1.name, "at", librarian1.library.name)
print("Book:", book1.title, "by", book1.author.name, "in", book1.library.name)
