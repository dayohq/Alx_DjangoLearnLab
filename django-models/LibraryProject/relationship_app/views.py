from django.shortcuts import render
from .models import Book

# Create your views here.


def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    return render(request, 'relationship_app/templates/relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(Detailview):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'