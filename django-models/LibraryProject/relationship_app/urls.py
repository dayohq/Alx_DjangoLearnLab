from django.urls import path
from .views import list_books, LibraryDetailView, user_login, user_logout, register

urlpatterns = [
    # Book-related views
    path('books/', list_books, name='list_books'), # Function-based view (FBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # Class-based View CBV

    # Authentication views
    path('login/', user_login, name='login/'),
    path('logout/', user_logout, name='logout'),
    path('register/', register, name='register'),
]