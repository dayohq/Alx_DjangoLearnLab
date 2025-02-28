from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import list_books, LibraryDetailView, register


urlpatterns = [
    # Book-related views
    path('books/', list_books, name='list_books'), # Function-based view (FBV)
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'), # Class-based View CBV

    # Authentication views
    path('login/', LoginView.as_view(template_name='authentication/login.html'), name='login'), # Django's built-in Login view
    path('logout/', LogoutView.as_view(template_name='authentication/logout.htmll'), name='logout'), # Django's built-in Logout view
    path('register/', register, name='register'),
]