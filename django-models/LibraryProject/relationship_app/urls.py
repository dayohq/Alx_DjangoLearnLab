from django.urls import path
from .views import list_books, LibraryDetailView

urlpatterns = [
    path('books/', list books, name='list_books'), # Function-based view (FBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # Class-based View CBV
]