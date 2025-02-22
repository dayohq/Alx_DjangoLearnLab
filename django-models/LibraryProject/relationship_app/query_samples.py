import django
import os

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)
    return books

# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

# Retrieve the librarian for a library
def librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except Library.DoesNotExist:
        return f"Library '{library_name}' not found."
    except Librarian.DoesNotExist:
        return f"No librarian assigned to '{library_name}'."

# Test queries
if __name__ == "__main__":
    print("Books by George Orwell:", books_by_author("George Orwell"))
    print("Books in Central Library:", books_in_library("Central Library"))
    print("Librarian of Central Library", librarian_for_library("Central Library"))
