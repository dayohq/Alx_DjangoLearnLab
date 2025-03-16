from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import BookSerializer
from .models import Book

# Create your views here.
class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    Allows unauthenticated access.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a book by ID.
    Allows unauthenticated access.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delet a book.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]