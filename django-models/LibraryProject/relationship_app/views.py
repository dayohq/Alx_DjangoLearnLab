from django.shortcuts import render
from .models import Book
from django.views.generic.detail import DetailView
# Create your views here.


def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    return render(request, 'relationship_app/templates/relationship_app/list_books.html', {'books': books})

from .models import Library

class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'