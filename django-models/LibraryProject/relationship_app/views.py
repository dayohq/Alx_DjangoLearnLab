from django.shortcuts import render
from django.views.generic import DetailView
from .models import Library, Book

# Create your views here.


def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    return render(request, 'list_books.html', {'books': books})

class LibraryDetailView(Detailview):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'