from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Book, Library
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


# Function-based View (FBV) to List Books
def list_books(request):
    """Function-based view to list all books."""
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Fixed template path


# Class-based View (CBV) for Library Detail
class LibraryDetailView(DetailView):
    """Class-based view to display details of a specific library."""
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# User Login View
def user_login(request):
    """Handles user authentication and login."""
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})


# User Logout View
def user_logout(request):
    """Logs out the user and redirects to the login page."""
    logout(request)
    return redirect('/login')  # Use named 'login' URL


# User Registration View
def register(request):
    """Handles user registration."""
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('register/') 
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})


# Helper functions to check roles
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == "Admin"

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == "Librarian"

def is_member(user):
    return user.is_authenticated and user.userprofile.role == "Member"

# View for Admins only
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# View for Librarians only
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# View for Members only
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')