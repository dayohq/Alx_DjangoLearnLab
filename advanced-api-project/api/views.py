from django.shortcuts import render

from .serializers import BookSerializer
from .models import Book

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from django_filters import rest_framework
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



# Create your views here.
class BookListView(generics.ListAPIView):
    """
    API view to retrieve a list of books.
    Allows unauthenticated access.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Enable Filtering, Searching, and Ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    # Define which fields can be filtered
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Define which fields can be searched
    search_fields = ['title', 'author__name']

    # Define which fields can be used for ordering
    ordering_fields = ['title', 'publication_year']



class BookDetailView(generics.RetrieveAPIView):
    """
    API view to retrieve a book by ID.
    Allows unauthenticated access.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    """
    API view to create a new book.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    API view to update an existing book.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    API view to delet a book.
    Requires authentication.
    """

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]