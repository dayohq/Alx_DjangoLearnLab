from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from django.http import HttpResponseForbidden
from .forms import BookForm

# Create your views here.
@permission_required('bookshelf.can_view_book', raise_exception=True)
def book_list(request):
    return HttpResponse("Welcome to my book shelf.")

def book_list(request):
    """Display all books securely with proper data handling"""
    books = Book.objects.all()
    return render(request, "bookshelf/book_list.html", {"books": books})

def book_detail(request, book_id):
    """Fetch book details safely"""
    book = get_object_or_404(Book, id=book_id)
    return render(request, "bookshelf/book_detail.html", {"book": book})

def add_book(request):
    """Securely handle user input using Django Forms"""
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "bookshelf/book_form.html", {"form": form})
