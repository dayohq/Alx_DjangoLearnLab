# CRUD Operations in Django Shell

## 1. Create a Book Instance
```python
from bookshelf.models import Book

book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)  # Expected Output: 1984 by George Orwell (1949)


retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title, retrieved_book.author, retrieved_book.publication_year)


book.title = "Nineteen Eighty-Four"
book.save()
print(Book.objects.get(id=book.id).title)


book.delete()
print(Book.objects.all())  # Expected Output: <QuerySet []> (empty)
