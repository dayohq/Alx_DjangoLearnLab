from bookshelf.models import Book

book.delete()
print(Book.objects.all())  # Expected Output: <QuerySet []> (empty)
