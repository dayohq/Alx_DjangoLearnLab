from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view, add_book, edit_book, delete_book
import relationship_app.views as views

urlpatterns = [
    # Book-related views
    path('books/', list_books, name='list_books'), # Function-based view (FBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # Class-based View CBV

    # Authentication views
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'), # Django's built-in Login view
    path('logout/', LogoutView.as_view(template_name='authentication/logout.htmll'), name='logout'), # Django's built-in Logout view
    path('register/', views.register, name='register'),

    #User Profile
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    path("add-book/", add_book, name="add_book"),
    path("edit-book/<int:book_id>/", edit_book, name="edit_book"),
    path("delete-book/<int:book_id>/", delete_book, name="delete_book"),    
]