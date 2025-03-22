from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status
from api.models import Book

class BookAPITestCase(APITestCase):

    def setUp(self):
        """Create test user and test books"""
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)  # Authenticate for protected routes

        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2000)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2010)

        self.book_url = "/api/books/"

    def test_get_book_list(self):
        """Test retrieving the list of books"""
        response = self.client.get(self.book_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return 2 books

    def test_create_book(self):
        """Test creating a new book"""
        data = {"title": "New Book", "author": "Author C", "publication_year": 2023}
        response = self.client.post(self.book_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        """Test updating a book's details"""
        update_data = {"title": "Updated Title", "author": "Updated Author", "publication_year": 2022}
        response = self.client.put(f"{self.book_url}{self.book1.id}/", update_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Title")

    def test_delete_book(self):
        """Test deleting a book"""
        response = self.client.delete(f"{self.book_url}{self.book1.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)  # Only 1 book should be left

    def test_filter_books(self):
        """Test filtering books by author"""
        response = self.client.get(f"{self.book_url}?author=Author A")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book One")

    def test_search_books(self):
        """Test searching books by title"""
        response = self.client.get(f"{self.book_url}?search=Two")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Book Two")

    def test_order_books(self):
        """Test ordering books by publication year"""
        response = self.client.get(f"{self.book_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Book One")  # Older book first

    def test_authentication_required(self):
        """Test that authentication is required for protected routes"""
        self.client.logout()  # Remove authentication
        response = self.client.post(self.book_url, {"title": "Test Book", "author": "Test Author", "publication_year": 2021})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Expect Unauthorized